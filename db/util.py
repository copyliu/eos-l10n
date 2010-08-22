#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from sqlalchemy.orm import eagerload

def cachedQuery(amount, *keywords):
    cache = {}

    def deco(function):
        def checkAndReturn(*args, **kwargs):
            kw = []
            for keyword in keywords:
                if keyword in kwargs:
                    kw.append(kwargs[keyword])

            kw = tuple(kw)
            cacheKey = (args[0:amount], kw)
            if cacheKey not in cache:
                cache[cacheKey] = function(*args, **kwargs)

            return cache[cacheKey]

        return checkAndReturn

    return deco


def processEager(eager):
    if eager == None:
        return tuple()
    else:
        l = []
        if isinstance(eager, basestring):
            eager = (eager,)

        for e in eager:
            l.append(eagerload(e))

        return l
