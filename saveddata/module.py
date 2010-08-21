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

from eos.modifiedAttributeDict import ModifiedAttributeDict, ItemAttrShortcut, ChargeAttrShortcut
from eos.effectHandlerHelpers import HandledItem, HandledCharge
from sqlalchemy.orm import validates, reconstructor
from itertools import chain

class State():
    OFFLINE = -1
    ONLINE = 0
    ACTIVE = 1
    OVERHEATED = 2

class Slot():
    LOW = 1
    MED = 2
    HIGH = 3
    RIG = 4
    SUBSYSTEM = 5

class Hardpoint():
    NONE = 0
    MISSILE = 1
    TURRET = 2

class Module(HandledItem, HandledCharge, ItemAttrShortcut, ChargeAttrShortcut):
    """An instance of this class represents a module together with its charge and modified attributes"""

    def __init__(self, item):
        self.__item = item if item != None else 0
        self.itemID = item.ID if item is not None else None
        self.__charge = 0
        self.projected = False
        self.state = State.ONLINE
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        if item != None:
            self.__itemModifiedAttributes.original = item.attributes
            self.__hardpoint = self.__calculateHardpoint(item)
            self.__slot = self.__calculateSlot(item)

        self.__chargeModifiedAttributes = ModifiedAttributeDict()

    @reconstructor
    def init(self):
        if self.dummySlot is None:
            self.__item = None
            self.__charge = None
        else:
            self.__slot = self.dummySlot
            self.__item = 0
            self.__charge = 0

    def __fetchItemInfo(self):
        import eos.db
        item = eos.db.getItem(self.itemID)
        self.__item = item
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = item.attributes
        self.__hardpoint = self.__calculateHardpoint(item)
        self.__slot = self.__calculateSlot(item)

    def __fetchChargeInfo(self):
        self.__chargeModifiedAttributes = ModifiedAttributeDict()
        if self.chargeID is not None:
            import eos.db
            charge = eos.db.getItem(self.chargeID)
            self.__charge = charge
            self.__chargeModifiedAttributes.original = charge.attributes
        else:
            self.__charge = 0

    @classmethod
    def buildEmpty(cls, slot):
        empty = Module(None)
        empty.__slot = slot
        empty.dummySlot = slot
        return empty

    def isEmpty(self):
        return self.item is None

    @property
    def hardpoint(self):
        if self.__item is None:
            self.__fetchItemInfo()

        return self.__hardpoint

    @property
    def maxRange(self):
        maxRange = self.item.getModifiedItemAttr("maxRange")
        if maxRange is not None: return maxRange
        else:
            delay = self.item.getModifiedItemAttr("explosionDelay")
            speed = self.item.getModifiedItemAttr("maxVelocity")
            if delay is not None and speed is not None:
                return delay * speed

    @property
    def slot(self):
        if self.__item is None:
            self.__fetchItemInfo()

        return self.__slot


    @property
    def itemModifiedAttributes(self):
        if self.__item is None:
            self.__fetchItemInfo()

        return self.__itemModifiedAttributes

    @property
    def chargeModifiedAttributes(self):
        if self.__charge is None:
            self.__fetchChargeInfo()

        return self.__chargeModifiedAttributes

    @property
    def item(self):
        if self.__item is None:
            self.__fetchItemInfo()

        return self.__item if self.__item != 0 else None

    @property
    def charge(self):
        if self.__charge is None:
            self.__fetchChargeInfo()

        return self.__charge if self.__charge != 0 else None

    @charge.setter
    def charge(self, charge):
        if not self.isValidCharge(charge): raise ValueError("Ammo does not fit in that slot")
        self.__charge = charge
        if charge is not None:
            self.chargeID = charge.ID
            self.__chargeModifiedAttributes.original = charge.attributes
        else:
            self.chargeID = None
            self.__chargeModifiedAttributes.original = None

        self.__itemModifiedAttributes.clear()

    def isValidCharge(self, charge):
        #Check sizes, if 'charge size > module volume' it won't fit
        if charge is None: return True
        chargeVolume = charge.getAttribute("volume")
        moduleCapacity = self.getModifiedItemAttr("capacity")
        if chargeVolume is not None and moduleCapacity is not None and chargeVolume > moduleCapacity:
            return False

        itemChargeSize = self.getModifiedItemAttr("chargeSize")
        if itemChargeSize is not None:
            chargeSize = charge.getAttribute('chargeSize')
            if itemChargeSize != chargeSize:
                return False

        chargeGroup = charge.groupID
        for i in range(5):
            itemChargeGroup = self.getModifiedItemAttr('chargeGroup' + str(i))
            if itemChargeGroup is None: continue
            if itemChargeGroup == chargeGroup: return True

        return False

    def __calculateHardpoint(self, item):
        effectHardpointMap = {"turretFitted" : Hardpoint.TURRET,
                              "useMissiles": Hardpoint.MISSILE}

        if item is None:
            return None

        for effectName, slot in effectHardpointMap.iteritems():
            if effectName in item.effects:
                return slot

        return Hardpoint.NONE

    def __calculateSlot(self, item):
        effectSlotMap = {"rigSlot" : Slot.RIG,
                         "loPower" : Slot.LOW,
                         "medPower" : Slot.MED,
                         "hiPower" : Slot.HIGH,
                         "subSystem" : Slot.SUBSYSTEM}
        if item is None:
            return None
        for effectName, slot in effectSlotMap.iteritems():
            if effectName in item.effects:
                return slot

        raise ValueError("Passed item does not fit in any known slot")

    @validates("ID", "itemID", "ammoID", "state")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "itemID" : lambda val: val is None or isinstance(val, int),
               "state" : lambda val: isinstance(val, int) and val >= -1 and val <= 2 and
                                     (val < 1 or self.item.isType("active")) and (val < 2 or self.item.isType("overheat")),
               "ammoID" : lambda val: isinstance(val, int)}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

    def clear(self):
        self.itemModifiedAttributes.clear()
        self.chargeModifiedAttributes.clear()

    def calculateModifiedAttributes(self, fit, runTime, forceProjected = False):
        #We will run the effect when two conditions are met:
        #1: It makes sense to run the effect
        #    The effect is either offline
        #    or the effect is passive and the module is in the online state (or higher)
        #    or the effect is active and the module is in the active state (or higher)
        #    or the effect is overheat and the module is in the overheated state (or higher)
        #2: the runtimes match
        if self.projected or forceProjected:
            context = "projected", "module"
            projected = True
        else:
            context = ("module",)
            projected = False

        for effect in self.item.effects.itervalues():
            if effect.runTime == runTime and \
            (effect.isType("offline") or
            (effect.isType("passive") and self.state >= State.ONLINE) or \
            (effect.isType("active") and self.state >= State.ACTIVE) or \
            (effect.isType("overheat") and self.state >= State.OVERHEATED)) and \
            ((projected and effect.isType("projected")) or not projected):
                    effect.handler(fit, self, context)

        if self.charge is not None and not projected:
            for effect in self.charge.effects.itervalues():
                if effect.runTime == runTime:
                    effect.handler(fit, self, ("moduleCharge",))

    def getCycleTime(self):
        speed =  self.getModifiedItemAttr("speed") or self.getModifiedItemAttr("duration")
        return speed / 1000.0 if speed is not None else speed

    def getCapUsage(self):
        speed = self.getCycleTime()
        if speed is not None:
            capUse = self.getModifiedItemAttr("capacitorNeed")
            if capUse is not None:
                speed = speed
                return capUse / speed

    def __deepcopy__(self, memo):
        copy = Module(self.item)
        copy.charge = self.charge
        copy.state = self.state
        return copy
