#===============================================================================
# Copyright (C) 2010 Diego Duclos
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
        # Base URL, limit Region to The Forge
        baseurl = "http://api.eve-central.com/api/marketstat?regionlimit=10000002&typeid={0}"
        # Generate request URL
        requrl = baseurl.format("&typeid=".join(map(lambda id: str(id), priceMap.iterkeys())))
        # Make the request object
        request = urllib2.Request(requrl, headers={"User-Agent" : "eos"})
        # Attempt to send request and shut up if everything goes wrong
        try:
            f = urllib2.urlopen(request)
        except:
            return
        # Parse the data we've got
        t = time.time()
        xml = minidom.parse(f)
        marketStat = xml.getElementsByTagName("marketstat").item(0)
        if marketStat is not None:
            types = marketStat.getElementsByTagName("type")
            for type in types:
                typeID = int(type.getAttribute("id"))
                sell = type.getElementsByTagName("sell").item(0)
                price = float(sell.getElementsByTagName("median").item(0).firstChild.data)
                p = priceMap[typeID]
                p.price = price
                p.time = t if price is not None else 0

    @classmethod
    def fetchC0rporation(cls, priceMap):
        """Use c0rporation.com price service provider"""
        # Our request url
        requrl = "http://prices.c0rporation.com/faction.xml"
        # Generate request
        request = urllib2.Request(requrl, headers={"User-Agent" : "eos"})
        # Attempt to send request and shut up if everything goes
        try:
            f = urllib2.urlopen(request)
        except:
            return
        # Parse the data we've got
        present = time.time()
        xml = minidom.parse(f)
        result = xml.getElementsByTagName("result").item(0)
        if result is not None:
            rowsets = xml.getElementsByTagName("rowset")
            for rowset in rowsets:
                rows = rowset.getElementsByTagName("row")
                # Go through all given data rows; as we don't want to request all data,
                # we need to process it in one single run
                for row in rows:
                    typeID = int(row.getAttribute("typeID"))
                    avgprice = float(row.getAttribute("avg"))
                    # Now let's get price object
                    priceobj = None
                    # If we have given typeID in the map we've got, pull price object out of it
                    if typeID in priceMap:
                        priceobj = priceMap[typeID]
                    # If we don't, request it from database
                    else:
                        priceobj = eos.db.getPrice(typeID)
                    # If everything failed, create price object ourselves and let session know about it
                    if priceobj is None:
                        priceobj = Price(typeID)
                        eos.db.add(priceobj)
                    # Finally, fill object with data
                    priceobj.price = avgprice
                    priceobj.time = present if avgprice is not None else 0
