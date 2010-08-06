#===============================================================================
# Copyright (C) 2010  Duclos Diego
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from model.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut
from model.effectHandlerHelpers import HandledItem

class Ship(ItemAttrShortcut, HandledItem):
    REQUIRED_ATTRIBUTES = ("cpuOutput", "powerOutput", "rechargeRate",
                              "scanResolution", "signatureRadius", "hp", "armorHP", "shieldCapacity",
                              "maxVelocity", "agility", "hiSlots", "medSlots", "lowSlots")

    def __init__(self, item):
        for requiredAttr in self.REQUIRED_ATTRIBUTES:
            if not requiredAttr in  item.attributes:
                raise ValueError("Passed item is not a ship, missing: %s" % requiredAttr)

        self.__item = item
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = item.attributes
        self.commandBonus = 0

    @property
    def item(self):
        return self.__item

    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes

    def clear(self):
        self.itemModifiedAttributes.clear()
        self.commandBonus = 0

    def calculateModifiedAttributes(self, fit, runTime, forceProjected = False):
        if forceProjected: return
        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime and effect.isType("passive"):
                 effect.handler(fit, self, ("ship",))

    def __deepcopy__(self, memo):
        copy = Ship(self.item)
        return copy
