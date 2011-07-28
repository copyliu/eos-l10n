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
    # Price validity period, 24 hours
    VALIDITY = 24*60*60
    # Re-request delay for failed fetches, 4 hours
    REREQUEST = 4*60*60

    def __init__(self, typeID):
        self.typeID = typeID
        self.time = 0
        self.failed = None
        self.__item = None

    @reconstructor
    def init(self):
        self.__item = None

    def isValid(self, present=time.time()):
        updateAge = present - self.time
        # Mark price as invalid if it is expired
        validity = updateAge <= self.VALIDITY
        # Price is considered as valid, if it's expired but we had failed
        # fetch attempt recently
        if validity is False and self.failed is not None:
            failedAge = present - self.failed
            validity = failedAge <= self.REREQUEST
            # If it's already invalid, it can't get any better
            if validity is False:
                return validity
            # If failed timestamp refers to future relatively to current
            # system clock, mark price as invalid
            if self.failed > present:
                return False
        # Do the same for last updated timestamp
        if self.time > present:
            return False
        return validity

    @classmethod
    def fetchPrices(cls, *prices):
        """Fetch all prices passed to this method"""
        # Set time of the request
        # We have to pass this time to all of our used methods, as multiple validity checks
        # Using time of check instead can make extremely rare edge-case bugs to appear
        # (e.g. when item price is already considered as outdated, but c0rp fetch is still
        # valid, just because their update time has been set using slightly older timestamp)
        present = time.time()
        # Dictionary for our price objects
        priceMap = {}
        # Check all provided price objects, and add invalid ones to dictionary
        for price in prices:
            if not price.isValid(present):
                # Those with market group go to eve-central, everything else to c0rporation
                priceMap[price.typeID] = price
        # Don't waste CPU if all prices are valid
        if len(priceMap) == 0:
            return
        # Set will contain items for which we've got no data after checking
        # all service. Added here just for sanity, will be overridden multiple times
        # inside services cycle
        noData = set()
        # List our price service methods
        services = (cls.fetchEveCentral, cls.fetchC0rporation)
        # Cycle through services
        for svc in services:
            # Request prices and get some feedback
            noData, abortedData = svc(priceMap, present)
            # Mark items with some failure occurred during fetching
            for typeID in abortedData:
                priceMap[typeID].failed = present
            # Clear map from the fetched and failed items, leaving only items
            # for which we've got no data
            toRemove = set()
            for typeID in priceMap:
                if typeID not in noData:
                    toRemove.add(typeID)
            for typeID in toRemove:
                del priceMap[typeID]
        # After we've checked all possible services, assign zero price for items
        # which were not found on any service to avoid re-fetches during validity
        # period
        for typeID in noData:
            priceMap[typeID].price = 0
            priceMap[typeID].time = present
            priceMap[typeID].failed = None

    @classmethod
    def fetchEveCentral(cls, priceMap, present=time.time()):
        """Use Eve-Central price service provider"""
        # This set will contain typeIDs which were requested but no data has been fetched for them
        noData = set()
        # This set will contain items for which data fetch was aborted due to technical reasons
        abortedData = set()
        # Set of items which are still to be requested
        typesToRequest = set()
        # Compose list of items we're going to request
        for typeID in priceMap:
            # Get item object
            item = eos.db.getItem(typeID)
            # We're not going to request items only with market group, as eve-central
            # doesn't provide any data for items not on the market
            # Items w/o market group will be added to noData in the very end
            if item.marketGroupID:
                typesToRequest.add(typeID)
        # Do not waste our time if all items are not on the market
        if len(typesToRequest) == 0:
            return (noData, abortedData)
        # This set will contain typeIDs for items which were in replies
        fetchedTypeIDs = set()
        # Base URL; limits prices to Jita solar system
        requrl = "http://api.eve-central.com/api/marketstat?usesystem=30000142"
        # As length of URL is limited, make a loop to make sure we request all data
        while(len(typesToRequest) > 0):
            # Set of items we're requesting during this cycle
            requestThisCycle = set()
            # Generate final URL, making sure it isn't longer than 255 characters
            for typeID in priceMap:
                newurl = "{0}&typeid={1}".format(requrl, typeID)
                if len(newurl) <= 255:
                    requrl = newurl
                    # Items which didn't make it into request are postponed until the next cycle
                    typesToRequest.remove(typeID)
                    # Fill the set for the utility needs
                    requestThisCycle.add(typeID)
                else:
                    break
            # Make the request object
            request = urllib2.Request(requrl, headers={"User-Agent" : "eos"})
            # Attempt to send request and process it
            try:
                data = urllib2.urlopen(request)
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
                            percprice = float(sell.getElementsByTagName("percentile").item(0).firstChild.data)
                        except (TypeError, ValueError):
                            percprice = 0
                        priceobj = priceMap[typeID]
                        priceobj.price = percprice
                        priceobj.time = present
                        priceobj.failed = None
            # If getting or processing data returned any errors, consider fetch
            # as aborted and move to the next one
            except:
                abortedData.update(requestThisCycle)
                continue
        # Get actual list of items for which we didn't get data
        noData.update(set(priceMap.iterkeys()).difference(fetchedTypeIDs).difference(abortedData))
        # And return it for future use
        return (noData, abortedData)

    @classmethod
    def fetchC0rporation(cls, priceMap, present=time.time()):
        """Use c0rporation.com price service provider"""
        # it must be here, otherwise eos doesn't load miscData in time
        from eos.types import MiscData
        # Set-container for requested items w/o any data returned
        noData = set()
        # Container for items which had errors during fetching
        abortedData = set()
        # Set with types for which we've got data
        fetchedTypeIDs = set()
        # Check when we updated prices last time
        fieldName = "priceC0rpTime"
        lastUpdatedField = eos.db.getMiscData(fieldName)
        # If this field isn't available, create and add it to session
        if lastUpdatedField is None:
            lastUpdatedField = MiscData(fieldName)
            eos.db.add(lastUpdatedField)
        # Convert field value to float, assigning it zero on any errors
        try:
            lastUpdated = float(lastUpdatedField.fieldValue)
        except (TypeError, ValueError):
            lastUpdated = 0
        # Get age of price
        updateAge = present - lastUpdated
        # Using timestamp we've got, check if fetch results are still valid and make
        # sure system clock hasn't been changed to past
        c0rpValidityUpd = updateAge <= cls.VALIDITY and lastUpdated <= present
        # If prices should be valid according to miscdata last update timestamp,
        # but method was requested to provide prices for some items, we can
        # safely assume that these items are not on the XML (to be more accurate,
        # on its previously fetched version), because all items which are valid
        # (and they are valid only when xml is valid) should be filtered out before
        # passing them to this method
        if c0rpValidityUpd is True:
            noData.update(set(priceMap.iterkeys()))
            return (noData, abortedData)
        # Check when price fetching failed last time
        fieldName = "priceC0rpFailed"
        # If it doesn't exist, add this one to the session too
        lastFailedField = eos.db.getMiscData(fieldName)
        if lastFailedField is None:
            lastFailedField = MiscData(fieldName)
            eos.db.add(lastFailedField)
        # Convert field value to float, assigning it none on any errors
        try:
            lastFailed = float(lastFailedField.fieldValue)
        except (TypeError, ValueError):
            lastFailed = None
        # If we had failed fetch attempt at some point
        if lastFailed is not None:
            failedAge = present - lastFailed
            # Check if we should refetch data now or not (we do not want to do anything until
            # refetch timeout is reached or we have failed timestamp referencing some future time)
            c0rpValidityFail = failedAge <= cls.REREQUEST and lastFailed <= present
            # If it seems we're not willing to fetch any data
            if c0rpValidityFail is True:
                # Consider all requested items as aborted. As we don't store list of items
                # provided by this service, this will include anything passed to this service,
                # even items which are usually not included in xml
                abortedData.update(set(priceMap.iterkeys()))
                return (noData, abortedData)
        # Our request url
        requrl = "http://prices.c0rporation.com/faction.xml"
        # Generate request
        request = urllib2.Request(requrl, headers={"User-Agent" : "eos"})
        # Attempt to send request and process returned data
        try:
            data = urllib2.urlopen(request)
            # Parse the data we've got
            xml = minidom.parse(data)
            rowsets = xml.getElementsByTagName("rowset")
            for rowset in rowsets:
                rows = rowset.getElementsByTagName("row")
                # Go through all given data rows; as we don't want to request and process whole xml
                # for each price request, we need to process it in one single run
                for row in rows:
                    typeID = int(row.getAttribute("typeID"))
                    # Add current typeID to the set of fetched types
                    fetchedTypeIDs.add(typeID)
                    # Median price field may be absent or empty, assign 0 in this case
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
                    priceobj.failed = None
            # Save current time for the future use
            lastUpdatedField.fieldValue = present
            # Clear the last failed field
            lastFailedField.fieldValue = None
            # Find which items were requested but no data has been returned
            noData.update(set(priceMap.iterkeys()).difference(fetchedTypeIDs))
            return (noData, abortedData)
        # If we failed somewhere during fetching or processing
        except:
            # Consider all items as aborted
            abortedData.update(set(priceMap.iterkeys()))
            # And whole fetch too
            lastFailedField.fieldValue = present
            return (noData, abortedData)
