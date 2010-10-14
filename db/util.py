#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
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

from sqlalchemy.orm import eagerload
from sqlalchemy.sql import and_

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

def processWhere(clause, where):
    if where is not None:
        if not hasattr(where, "__iter__"):
            where = (where,)

        for extraClause in where:
            clause = and_(clause, extraClause)

    return clause
