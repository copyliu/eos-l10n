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

import eos.types

class HandledList(list):
    def filteredItemIncrease(self, filter, *args, **kwargs):
        for element in self:
            try:
                if filter(element):
                    element.increaseItemAttr(*args, **kwargs)
            except AttributeError:
                pass

    def filteredItemMultiply(self, filter, *args, **kwargs):
        for element in self:
            try:
                if filter(element):
                    element.multiplyItemAttr(*args, **kwargs)
            except AttributeError:
                pass

    def filteredItemBoost(self, filter, *args, **kwargs):
        for element in self:
            try:
                if filter(element):
                    element.boostItemAttr(*args, **kwargs)
            except AttributeError:
                pass

    def filteredChargeIncrease(self, filter, *args, **kwargs):
        for element in self:
            try:
                if filter(element):
                    element.increaseChargeAttr(*args, **kwargs)
            except AttributeError:
                pass

    def filteredChargeMultiply(self, filter, *args, **kwargs):
        for element in self:
            try:
                if filter(element):
                    element.multiplyChargeAttr(*args, **kwargs)
            except AttributeError:
                pass

    def filteredChargeBoost(self, filter, *args, **kwargs):
        for element in self:
            try:
                if filter(element):
                    element.boostChargeAttr(*args, **kwargs)
            except AttributeError:
                pass

class HandledModuleList(HandledList):
    def append(self, mod):
        emptyPosition = float("Inf")
        for i in xrange(len(self)):
            currMod = self[i]
            if currMod.isEmpty and not mod.isEmpty and currMod.slot == mod.slot:
                currPos = mod.position or i
                if currPos < emptyPosition:
                    emptyPosition = currPos

        if emptyPosition < len(self):
            del self[emptyPosition]
            mod.position = emptyPosition
            HandledList.insert(self, emptyPosition, mod)
            return

        mod.position = len(self)
        HandledList.append(self, mod)

    def insert(self, index, mod):
        mod.position = index
        i = index
        while i < len(self):
            self[i].position += 1
            i += 1
        HandledList.insert(self, index, mod)

    def remove(self, mod):
        HandledList.remove(self, mod)
        oldPos = mod.position

        mod.position = None
        for i in xrange(oldPos, len(self)):
            self[i].position -= 1

    def toDummy(self, index):
        mod = self[index]
        if not mod.isEmpty:
            dummy = eos.types.Module.buildEmpty(mod.slot)
            dummy.position = index
            self[index] = dummy

class HandledDroneList(HandledList):
    def __init__(self):
        self._findCache = {}

    def find(self, item):
        if self._findCache.has_key(item.ID):
            return self._findCache[item.ID]
        else:
            return None

    def append(self, drone):
        list.append(self, drone)
        self._findCache[drone.item.ID] = drone

    def remove(self, drone):
        if self._findCache.has_key(drone.item.ID):
            del self._findCache[drone.item.ID]
            HandledList.remove(self, drone)
        else:
            raise KeyError("Drone is not in the list")

    def appendItem(self, item, amount = 1):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.find(item)
        if d is None:
            d = eos.types.Drone(item)
            self.append(d)

        d.amount += amount
        return d

    def removeItem(self, item, amount):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.find(item)
        if d is None: return
        d.amount -= amount
        if d.amount <= 0:
            self.remove(d)
            return None

        return d


class HandledImplantBoosterList(HandledList):
    def __init__(self):
        self.__slotCache = {}

    def append(self, booster, replace = False):
        if self.__slotCache.has_key(booster.slot):
            if replace: self.remove(booster)
            else:
                if replace: self.remove(booster)
                else: raise ValueError("Booster/Implant slot already in use, remove the old one first or set replace = True")

        list.append(self, booster)


class HandledProjectedModList(HandledList):
    def append(self, proj):
        proj.projected = True
        HandledList.append(self, proj)

class HandledProjectedDroneList(HandledDroneList):
    def append(self, proj):
        proj.projected = True
        if self._findCache.has_key(proj.item.ID):
            raise ValueError("Drone already here, cannot add the same one multiple times")

        list.append(self, proj)
        self._findCache[proj.item.ID] = proj

class HandledProjectedFitList(list):
    """
    Use list here, handledList kills sqlalchemy for some unknown reason.
    """
    def append(self, proj):
        proj.projected = True
        list.append(self, proj)

class HandledItem(object):
    def increaseItemAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.increase(*args, **kwargs)

    def multiplyItemAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.multiply(*args, **kwargs)

    def boostItemAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.boost(*args, **kwargs)

class HandledCharge(object):
    def increaseChargeAttr(self, *args, **kwargs):
        self.chargeModifiedAttributes.increase(*args, **kwargs)

    def multiplyChargeAttr(self, *args, **kwargs):
        self.chargeModifiedAttributes.multiply(*args, **kwargs)

    def boostChargeAttr(self, *args, **kwargs):
        self.chargeModifiedAttributes.boost(*args, **kwargs)
