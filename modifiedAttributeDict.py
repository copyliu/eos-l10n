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

from math import exp

class ItemAttrShortcut(object):
    def getModifiedItemAttr(self, key):
        if key in self.itemModifiedAttributes:
            return self.itemModifiedAttributes[key]
        else:
            return None


class ChargeAttrShortcut(object):
    def getModifiedChargeAttr(self, key):
        if key in self.chargeModifiedAttributes:
            return self.chargeModifiedAttributes[key]
        else:
            return None


class ModifiedAttributeDict(object):
    class CalculationPlaceholder():
        pass

    def __init__(self, fit = None):
        self.__modified = {}
        self.__original = None
        self.__intermediary = {}
        self.__preIncreases = {}
        self.__postIncreases = {}
        self.__multipliers = {}
        self.__penalizedMultipliers = {}
        self.__affectedBy = {}
        self.__forced = {}
        self.fit = fit

    def clear(self):
        self.__intermediary.clear()
        self.__modified.clear()
        self.__preIncreases.clear()
        self.__postIncreases.clear()
        self.__multipliers.clear()
        self.__penalizedMultipliers.clear()
        self.__affectedBy.clear()
        self.__forced.clear()

    @property
    def original(self):
        return self.__original

    @original.setter
    def original(self, val):
        self.__original = val
        self.__modified.clear()

    def __getitem__(self, key):
        if key in self.__forced:
            return self.__forced[key]
        elif key in self.__modified:
            if self.__modified[key] == self.CalculationPlaceholder:
                self.__modified[key] = self.__calculateValue(key)
            return self.__modified[key]
        elif key in self.__intermediary:
            return self.__intermediary[key]
        else:
            return self.getOriginal(key)

    def getOriginal(self, key):
        val = self.__original[key]
        return val.value if hasattr(val, "value") else val

    def __setitem__(self, key, val):
        self.__intermediary[key] = val

    def __iter__(self):
        all = dict(self.__original, **self.__modified)
        return (key for key in all)

    def __contains__(self, key):
        return (self.__original is not None and key in self.__original) or key in self.__modified

    def iterkeys(self):
        for key in self:
            yield key

    def itervalues(self):
        for key in self:
            yield self[key]

    def iteritems(self):
        for key in self:
            yield key, self[key]

    iter = __iter__
    items = iteritems
    keys = iterkeys
    values = itervalues

    def __placehold(self, key):
        if key in self.__modified and self.__modified[key] != self.CalculationPlaceholder:
            self.__intermediary[key] = self.__modified[key]

        self.__modified[key] = self.CalculationPlaceholder

    def __calculateValue(self, key):
        #Grab our values if they're there, otherwise we'll take default values.
        preIncrease = self.__preIncreases[key] if key in self.__preIncreases else 0
        postIncrease = self.__postIncreases[key] if key in self.__postIncreases else 0
        multiplier = self.__multipliers[key] if key in self.__multipliers else 1
        penalizedMultiplierGroups = self.__penalizedMultipliers[key] if key in self.__penalizedMultipliers else {}
        val = self.__intermediary[key] if key in self.__intermediary else self.getOriginal(key) if key in self.__original else 0
        #We'll do stuff in the following order:
        #Preincreass, then multipliers
        #then stacking penalized multipliers, then postIncreases
        val += preIncrease
        val *= multiplier

        if len(penalizedMultiplierGroups) > 0:
            #Each group is penalized independantly
            #Things in different groups will not be stack penaltied between eachother
            for penalizedMultipliers in penalizedMultiplierGroups.itervalues():
                #A quick explanation of how this works:
                #1: Bonusses and penalties are penalized seperatly, so we'll have to filter each of them
                l1 = filter(lambda val: val > 1, penalizedMultipliers)
                l2 = filter(lambda val: val < 1, penalizedMultipliers)
                #2: The most significant bonusses take the smallest penalty,
                #This means we'll have to sort
                abssort = lambda val: -abs(val - 1)
                l1.sort(key=abssort)
                l2.sort(key=abssort)
                #3: The first module doesn't get penaltied at all
                #Any modul after the first takes penalties according to:
                #1 + (multplier - 1) * math.exp(- math.pow(i, 2) / 7.1289)
                for l in (l1, l2):
                    for i in xrange(len(l)):
                        bonus = l[i]
                        val *= 1 + (bonus - 1) * exp(- i ** 2 / 7.1289)

        val += postIncrease
        return val

    def getAfflictions(self, key):
        return self.__affectedBy[key] if key in self.__affectedBy else {}

    def __afflict(self, key):
        if self.fit is None:
            return

        if key not in self.__affectedBy:
            self.__affectedBy[key] = {}

        stuff = self.__affectedBy[key]
        if self.fit not in stuff:
            stuff[self.fit] = {}

        stuff = stuff[self.fit]
        modifier = self.fit.getModifier()
        if modifier not in stuff:
            stuff[modifier] = []



    def increase(self, attributeName, increase, position="pre"):
        if position == "pre":
            tbl = self.__preIncreases

        elif position == "post":
            tbl = self.__postIncreases

        else:
            raise ValueError("position should be either pre or post")

        if not attributeName in tbl:
            tbl[attributeName] = 0

        tbl[attributeName] += increase
        self.__placehold(attributeName)
        self.__afflict(attributeName)

    def multiply(self, attributeName, multiplier, stackingPenalties=False, penaltyGroup="default"):
        if stackingPenalties:
            if not attributeName in self.__penalizedMultipliers:
                self.__penalizedMultipliers[attributeName] = {}
            if not penaltyGroup in self.__penalizedMultipliers[attributeName]:
                self.__penalizedMultipliers[attributeName][penaltyGroup] = []

            tbl = self.__penalizedMultipliers[attributeName][penaltyGroup]
            tbl.append(multiplier)
        else:
            if not attributeName in self.__multipliers:
                self.__multipliers[attributeName] = 1
            self.__multipliers[attributeName] *= multiplier

        self.__placehold(attributeName)
        self.__afflict(attributeName)

    def boost(self, attributeName, boostFactor, *args, **kwargs):
        self.multiply(attributeName, 1 + boostFactor / 100.0, *args, **kwargs)

    def force(self, attributeName, value):
        self.__forced[attributeName] = value

class Affliction():
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
