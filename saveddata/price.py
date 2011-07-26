#===============================================================================
# Copyright (C) 2010 Diego Duclos
# Copyright (C) 2011 Anton Vorobyov
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================


import time
import urllib2
from xml.dom import minidom

from sqlalchemy.orm import reconstructor

import eos.db

class Price(object):
    VALIDITY = 24*60*60

    def __init__(self, typeID):
        self.time = 0
        self.typeID = typeID
        self.__item = None

    @reconstructor
    def init(self):
        self.__item = None

    @property
    def isValid(self):
        present = time.time()
        age = present - self.time
        # Mark price as invalid if time expired or entry was created in future
        validity = age < self.VALIDITY and present > self.time
        return validity

    @classmethod
    def fetchPrices(cls, *prices):
        """Fetch all prices passed to this method"""
        # Dictionaries to store our price objects
        # Format: { typeID : price }
        priceMapEvec = {}
        priceMapC0rp = {}
        # Check all provided price objects, and add invalid ones to dictionary
        for price in prices:
            if not price.isValid:
                # Those with market group go to eve-central, everything else to c0rporation
                item = eos.db.getItem(price.typeID)
                if item.marketGroupID:
                    priceMapEvec[price.typeID] = price
                else:
                    priceMapC0rp[price.typeID] = price

        if len(priceMapEvec) > 0:
            noData = cls.fetchEveCentral(priceMapEvec)
            # If data hasn't been returned for any requested item, let's try to request it
            # from the next service
            if len(noData) > 0:
                for typeID in noData:
                    priceMapC0rp[typeID] = priceMapEvec[typeID]
        if len(priceMapC0rp) > 0:
            noData = cls.fetchC0rporation(priceMapC0rp)
            # If we didn't get data for some of the items from all our price service
            # providers, assign it zero price to avoid re-fetches during validity period
            if len(noData) > 0:
                present = time.time()
                for typeID in noData:
                    priceobj = priceMapC0rp[typeID]
                    priceobj.price = 0
                    priceobj.time = present

    @classmethod
    def fetchEveCentral(cls, priceMap):
        """Use Eve-Central price service provider"""
        # Set time of the request
        present = time.time()
        # Set of items which are still to be requested
        typesToRequest = set(priceMap.iterkeys())
        # This set will contain typeIDs for items which were in replies
        fetchedTypeIDs = set()
        # This set will contain typeIDs which were requested but no data has been fetched for them
        noData = set()
        # Base URL; limits prices to The Forge region
        requrl = "http://api.eve-central.com/api/marketstat?regionlimit=10000002"
        # As length of URL is limited, make a loop to make sure we request all data
        while(len(typesToRequest) > 0):
            # Generate final URL, making sure it isn't longer than 255 characters
            # Items which didn't make it into request are postponed until the next cycle
            for typeID in priceMap:
                newurl = "{0}&typeid={1}".format(requrl, typeID)
                if len(newurl) <= 255:
                    requrl = newurl
                    typesToRequest.remove(typeID)
                else:
                    break
            # Make the request object
            request = urllib2.Request(requrl, headers={"User-Agent" : "eos"})
            # Attempt to send request and go to next request cycle
            # if anything goes wrong
            try:
                data = urllib2.urlopen(request)
            except:
                continue
            # Parse the data we've got
            xml = minidom.parse(data)
            marketStat = xml.getElementsByTagName("marketstat").item(0)
            if marketStat is not None:
                types = marketStat.getElementsByTagName("type")
                # Cycle through all types we've got from request
                for type in types:
                    # Get data out of each typeID details tree
                    typeID = int(type.getAttribute("id"))
                    sell = type.getElementsByTagName("sell").item(0)
                    # Add item id to list of fetched items
                    fetchedTypeIDs.add(typeID)
                    # If price data was none, set it to zero to avoid re-requesting it
                    try:
                        medprice = float(sell.getElementsByTagName("median").item(0).firstChild.data)
                    except (TypeError, ValueError):
                        medprice = 0
                    priceobj = priceMap[typeID]
                    priceobj.price = medprice
                    priceobj.time = present
        # Get actual list of items for which we didn't get data
        noData.update(set(priceMap.iterkeys()).difference(fetchedTypeIDs))
        # And return it for future use
        return noData

    @classmethod
    def fetchC0rporation(cls, priceMap):
        """Use c0rporation.com price service provider"""
        # Set time of the request
        present = time.time()
        # Set-container for requested items w/o any data returned
        noData = set()
        # Check when we updated prices last time
        fieldName = "priceC0rpTime"
        lastUpdatedField = eos.db.getMiscData(fieldName)
        # If this field isn't available, create and add it to session
        if lastUpdatedField is None:
            from eos.types import MiscData
            lastUpdatedField = MiscData(fieldName)
            eos.db.add(lastUpdatedField)
        # Convert field value to float, assigning it zero on any errors
        try:
            lastUpdated = float(lastUpdatedField.fieldValue)
        except (TypeError, ValueError):
            lastUpdated = 0
        age = present - lastUpdated
        # Using timestamps we've got, check if fetch results are still valid
        # and make sure system clock wasn't changed to past
        if age < cls.VALIDITY and present > lastUpdated:
            # Return all requested typeIDs as items with no price data
            # As we pre-check for validity before passing prices to price service,
            # valid prices should never get into here and it's safe to assume that
            # prices which are not on the xml were requested
            noData.update(set(priceMap.iterkeys()))
            return noData
        # Our request url
        requrl = "http://prices.c0rporation.com/faction.xml"
        # Generate request
        request = urllib2.Request(requrl, headers={"User-Agent" : "eos"})
        # Attempt to send request and return list of items we've failed to get
        # data for if anything goes wrong
        try:
            data = urllib2.urlopen(request)
        except:
            noData.update(set(priceMap.iterkeys()))
            return noData
        # Set with types for which we've got data
        fetchedTypeIDs = set()
        # Parse the data we've got
        xml = minidom.parse(data)
        result = xml.getElementsByTagName("result").item(0)
        if result is not None:
            rowsets = xml.getElementsByTagName("rowset")
            for rowset in rowsets:
                rows = rowset.getElementsByTagName("row")
                # Go through all given data rows; as we don't want to request and process whole xml
                # for each price request, we need to process it in one single run
                for row in rows:
                    typeID = int(row.getAttribute("typeID"))
                    # Add current typeID to the set of fetched types
                    fetchedTypeIDs.add(typeID)
                    # Average price field may be absent or empty, assign 0 in this case
                    try:
                        medprice = float(row.getAttribute("median"))
                    except (TypeError, ValueError):
                        medprice = 0
                    # Now let's get price object
                    priceobj = None
                    # If we have given typeID in the map we've got, pull price object out of it
                    if typeID in priceMap:
                        priceobj = priceMap[typeID]
                    # If we don't, request it from database
                    else:
                        priceobj = eos.db.getPrice(typeID)
                    # If everything failed
                    if priceobj is None:
                        # Create price object ourselves
                        priceobj = Price(typeID)
                        # And let database know that we'd like to keep it
                        eos.db.add(priceobj)
                    # Finally, fill object with data
                    priceobj.price = medprice
                    priceobj.time = present
        # Save current time for the future use
        lastUpdatedField.fieldValue = present
        # Find which items were requested but no data has been returned
        noData.update(set(priceMap.iterkeys()).difference(fetchedTypeIDs))
        return noData
