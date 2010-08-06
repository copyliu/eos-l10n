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
from sqlalchemy.orm import validates, reconstructor
class Implant(HandledItem, ItemAttrShortcut):
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.__item = item
        self.itemID = item.ID
        self.active = True
        self.build()

    @reconstructor
    def init(self):
        from model import db
        self.__item = db.getItem(self.itemID)
        self.__slot = self.__calculateSlot(self.__item)
        self.build()

    def build(self):
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = self.item.attributes

    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes

    @property
    def slot(self):
        return self.__slot

    @property
    def item(self):
        return self.__item

    def __calculateSlot(self, item):
        if not "implantness" in item.attributes:
            raise ValueError("Passed item is not an implant")

        return int(item.attributes["implantness"].value)

    def clear(self):
        self.itemModifiedAttributes.clear()

    def calculateModifiedAttributes(self, fit, runTime, forceProjected = False):
        if forceProjected: return
        if self.active == False: return
        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime and effect.isType("passive"):
                effect.handler(fit, self, ("implant",))

    @validates("fitID", "itemID", "active")
    def validator(self, key, val):
        map = {"fitID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int),
               "active": lambda val: isinstance(val, bool)}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

    def __deepcopy__(self, memo):
        copy = Implant(self.item)
        copy.active = self.active
        return copy
