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

from eos.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut
from eos.effectHandlerHelpers import HandledItem
from sqlalchemy.orm import reconstructor, validates

class Booster(HandledItem, ItemAttrShortcut):
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.itemID = item.ID
        self.__item = item
        self.active = True
        self.build()

    @reconstructor
    def init(self):
        self.__item = None

    def build(self):
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = self.__item.attributes
        self.__sideEffects = []
        for effect in self.item.effects.itervalues():
            if effect.isType("boosterSideEffect"):
                s = SideEffect(self)
                s.effect = effect
                s.active = effect.ID in self.__activeSideEffectIDs
                self.__sideEffects.append(s)

    def __fetchItemInfo(self):
        import eos.db
        self.__item = eos.db.getItem(self.itemID)
        self.__slot = self.__calculateSlot(self.__item)
        self.build()

    def iterSideEffects(self):
        return self.__sideEffects.__iter__()

    def getSideEffect(self, name):
        for sideEffect in self.iterSideEffects():
            if sideEffect.effect.name == name:
                return sideEffect

        raise KeyError("SideEffect with %s as name not found" % name)

    @property
    def itemModifiedAttributes(self):
        if self.__item is None:
            self.__fetchItemInfo()

        return self.__itemModifiedAttributes

    @property
    def slot(self):
        if self.__item is None:
            self.__fetchItemInfo()

        return self.__slot

    @property
    def item(self):
        if self.__item is None:
            self.__fetchItemInfo()

        return self.__item

    def __calculateSlot(self, item):
        if not "boosterness" in item.attributes:
            raise ValueError("Passed item is not a booster")

        return int(item.attributes["boosterness"].value)

    def clear(self):
        self.itemModifiedAttributes.clear()

    def calculateModifiedAttributes(self, fit, runTime, forceProjected = False):
        if forceProjected: return
        if self.active == False: return
        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime and effect.isType("passive"):
                effect.handler(fit, self, ("booster",))

        for sideEffect in self.iterSideEffects():
            if sideEffect.active and sideEffect.effect.runTime == runTime:
                sideEffect.effect.handler(fit, self, ("boosterSideEffect",))

    @validates("ID", "itemID", "ammoID", "active")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "itemID" : lambda val: isinstance(val, int),
               "ammoID" : lambda val: isinstance(val, int),
               "active" : lambda val: isinstance(val, bool),
               "slot" : lambda val: isinstance(val, int) and val >= 1 and val <= 3}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

    def __deepcopy__(self, memo):
        copy = Booster(self.item)
        copy.active = self.active
        origSideEffects = list(self.iterSideEffects())
        copySideEffects = list(copy.iterSideEffects())
        i = 0
        while i < len(origSideEffects):
            copySideEffects[i].active = origSideEffects[i].active
            i += 1

        return copy


class SideEffect(object):
    def __init__(self, owner):
        self.__owner = owner
        self.__active = False
        self.__effect = None

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        if not isinstance(active, bool):
            raise TypeError("Expecting a bool, not a " + type(active))

        if active != self.__active:
            if active:
                self.__owner._Booster__activeSideEffectIDs.append(self.effect.ID)
            else:
                self.__owner._Booster__activeSideEffectIDs.remove(self.effect.ID)

            self.__active = active

    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, effect):
        if not hasattr(effect, "handler"):
            raise TypeError("Need an effect with a handler")

        self.__effect = effect
