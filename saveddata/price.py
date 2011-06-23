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

    @classmethod
    def fetchEveCentral(cls, priceMap):
        """Use Eve-Central price service provide"""
        REQUEST_URL = "http://api.eve-central.com/api/marketstat?regionlimit=10000002&typeid=%s"

        request = urllib2.Request(REQUEST_URL % "&typeid=".join(map(lambda id: str(id), priceMap.iterkeys())),
                                  None, {"User-Agent" : "eos"})

        try:
            f = urllib2.urlopen(request)
        except:
            return

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
