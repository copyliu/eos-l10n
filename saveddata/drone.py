#===============================================================================
# Copyright (C) 2010 Diego Duclos
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

from model.types import Item
from model.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut, ChargeAttrShortcut
from model.effectHandlerHelpers import HandledItem, HandledCharge
from sqlalchemy.orm import validates, reconstructor
class Drone(HandledItem, HandledCharge, ItemAttrShortcut, ChargeAttrShortcut):
    def __init__(self, item):
        if item.category.name != "Drone":
            raise ValueError("Passed item is not a drone")

        self.__item = item
        self.itemID = item.ID
        self.amount = 0
        self.amountActive = 0
        self.projected = False
        self.build()

    @reconstructor
    def init(self):
        from model import db
        self.__item = db.getItem(self.itemID)
        self.build()

    def build(self):
        from model import db
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.itemModifiedAttributes.original = self.item.attributes
        chargeID = self.getModifiedItemAttr("entityMissileTypeID")
        if chargeID != None:
            charge = db.getItem(int(chargeID))
            self.__charge = charge
            self.__chargeModifiedAttributes = ModifiedAttributeDict()
            self.chargeModifiedAttributes.original = charge.attributes
        else:
            self.__charge = self.__item
            self.__chargeModifiedAttributes = self.__itemModifiedAttributes

    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes

    @property
    def chargeModifiedAttributes(self):
        return self.__chargeModifiedAttributes

    @property
    def item(self):
        return self.__item

    @property
    def charge(self):
        return self.__charge

    @validates("ID", "itemID", "chargeID", "amount", "amountActive")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int),
               "chargeID" : lambda val: isinstance(val, int),
               "amount" : lambda val: isinstance(val, int) and val >= 0,
               "amountActive" : lambda val: isinstance(val, int) and val <= self.amount and val >= 0}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

    def clear(self):
        self.itemModifiedAttributes.clear()
        self.chargeModifiedAttributes.clear()

    def calculateModifiedAttributes(self, fit, runTime, forceProjected = False):
        if self.projected or forceProjected:
            context = "projected", "drone"
            projected = True
        else:
            context = ("drone",)
            projected = False

        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime and \
            ((projected == True and effect.isType("projected")) or \
             projected == False and effect.isType("passive")):
                i = 0
                while i != self.amountActive:
                    effect.handler(fit, self, context)
                    i += 1

        if self.charge:
            for effect in self.charge.effects.itervalues():
                if effect.runTime == runTime:
                    effect.handler(fit, self, ("droneCharge",))

    def __deepcopy__(self, memo):
        copy = Drone(self.item)
        copy.amount = self.amount
        copy.amountActive = self.amountActive
        return copy
