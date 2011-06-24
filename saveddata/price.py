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
            cls.fetchEveCentral(priceMapEvec)
        if len(priceMapC0rp) > 0:
            cls.fetchC0rporation(priceMapC0rp)

    @classmethod
    def fetchEveCentral(cls, priceMap):
        """Use Eve-Central price service provider"""
        # Set time of the request
        present = time.time()
        # Set of items which are still to be requested
        typesToRequest = set(priceMap.iterkeys())
        # This set will contain typeIDs for items which were in replies
        fetchedTypeIDs = set()
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
            # if everything goes wrong
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
        # Find which items were requested but no data has been returned
        noData = set(priceMap.iterkeys()).difference(fetchedTypeIDs)
        # By setting price to zero make sure we do not re-request them during validity period
        for typeID in noData:
            priceobj = priceMap[typeID]
            priceobj.price = 0
            priceobj.time = present

    @classmethod
    def fetchC0rporation(cls, priceMap):
        """Use c0rporation.com price service provider"""
        # Set time of the request
        present = time.time()
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
            # Do nothing if results are valid
            return
        # Our request url
        requrl = "http://prices.c0rporation.com/faction.xml"
        # Generate request
        request = urllib2.Request(requrl, headers={"User-Agent" : "eos"})
        # Attempt to send request and shut up if everything goes
        try:
            data = urllib2.urlopen(request)
        except:
            return
        # Parse the data we've got
        xml = minidom.parse(data)
        result = xml.getElementsByTagName("result").item(0)
        if result is not None:
            rowsets = xml.getElementsByTagName("rowset")
            for rowset in rowsets:
                rows = rowset.getElementsByTagName("row")
                # Go through all given data rows; as we don't want to request all data,
                # we need to process it in one single run
                for row in rows:
                    typeID = int(row.getAttribute("typeID"))
                    # Average price field may be absent or empty, assign 0 in this case
                    try:
                        avgprice = float(row.getAttribute("avg"))
                    except (TypeError, ValueError):
                        avgprice = 0
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
                    priceobj.price = avgprice
                    priceobj.time = present
        # Save current time for the future use
        lastUpdatedField.fieldValue = present
