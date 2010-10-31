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

from sqlalchemy.orm import eagerload
from sqlalchemy.sql import and_

replace = {"attributes": "_Item__attributes"}
def processEager(eager):
    if eager == None:
        return tuple()
    else:
        l = []
        if isinstance(eager, basestring):
            eager = (eager,)

        for e in eager:
            l.append(eagerload(_replacements(e)))

        return l

def _replacements(e):
    for r in replace:
        l = len(r)
        if e[0:l] == r:
            return _replacements(replace[r] + e[l:])
        original = ".%s" % r
        l = len(original)
        if e[-l:] == original:
            return _replacements(e[:-l] + ".%s" % replace[r])
        original = ".%s." % r
        if original in e:
            return _replacements(str.replace(original, ".%s." % replace[r]))

    return e

def processWhere(clause, where):
    if where is not None:
        if not hasattr(where, "__iter__"):
            where = (where,)

        for extraClause in where:
            clause = and_(clause, extraClause)

    return clause
