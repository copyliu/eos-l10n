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

from sqlalchemy.orm import reconstructor
import urllib2
from xml.dom import minidom
import time

class Price(object):
    REQUEST_URL = "http://api.eve-central.com/api/marketstat?regionlimit=10000002&typeid=%s"
    VALIDITY = 86400

    def __init__(self, typeID):
        self.time = 0
        self.typeID = typeID
        self.__item = None

    @reconstructor
    def init(self):
        self.__item = None

    @property
    def isValid(self):
        return time.time() - self.time < self.VALIDITY

    @classmethod
    def fetchPrices(cls, *prices):
        """Fetch all prices passed to this method"""

        priceObjByTypeID = {}
        for price in prices:
            if not price.isValid:
                priceObjByTypeID[price.typeID] = price

        if len(priceObjByTypeID) == 0:
            return

        request = urllib2.Request(cls.REQUEST_URL % "&typeid=".join(map(lambda id: str(id), priceObjByTypeID.iterkeys())),
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
                p = priceObjByTypeID[typeID]
                p.price = price
                p.time = t if price is not None else 0
