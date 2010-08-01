#===============================================================================
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

from model.effectHandlerHelpers import HandledList
from model.modifiedAttributeDict import ModifiedAttributeDict
from sqlalchemy.orm import validates, reconstructor
from itertools import chain

class Fit(object):
    """Represents a fitting, with modules, ship, implants, etc."""
    EXTRA_ATTRIBUTES = {"armorRepair": 0,
                        "hullRepair": 0,
                        "shieldRepair": 0,
                        "capBoost": 0,
                        "capDrain": 0,
                        "maxActiveDrones": 0,
                        "maxTargetsLocked": 0,
                        "droneControlRange": 0,
                        "cloaked": False}

    def __init__(self):
        self.__modules = HandledList()
        self.__drones = HandledDroneList()
        self.__implants = HandledImplantBoosterList()
        self.__boosters = HandledImplantBoosterList()
        self.__projectedModules = HandledList()
        self.__projectedFits = HandledList()
        self.__character = None
        self.__owner = None
        self.shipID = None
        self.projected = False
        self.name = ""
        self.build()

    @reconstructor
    def init(self):
        self.build()

    def build(self):
        from model import db
        self.__calculated = False
        self.__calculatedTargets = []
        self.__ship = Ship(db.getItem(self.shipID)) if self.shipID != None else None
        self.extraAttributes = ModifiedAttributeDict()
        self.extraAttributes.original = self.EXTRA_ATTRIBUTES

    @property
    def character(self):
        return self.__character if self.__character != None else Character.getAll0()

    @character.setter
    def character(self, char):
        self.__character = char

    @property
    def ship(self):
        return self.__ship

    @ship.setter
    def ship(self, ship):
        self.__ship = ship
        self.shipID = ship.item.ID if ship != None else None

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def drones(self):
        return self.__drones

    @property
    def modules(self):
        return self.__modules

    @property
    def implants(self):
        return self.__implants

    @property
    def boosters(self):
        return self.__boosters

    @property
    def projectedModules(self):
        return self.__projectedModules

    @property
    def projectedFits(self):
        return self.__projectedFits

    @property
    def projectedDrones(self):
        return self.__projectedDrones

    @validates("ID", "ownerID", "shipID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "ownerID" : lambda val: isinstance(val, int),
               "shipID" : lambda val: isinstance(val, int) or val == None}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

    def clear(self):
        self.__calculated = False
        del self.__calculatedTargets[:]
        if self.ship != None: self.ship.clear()
        c = chain(self.modules, self.drones, self.boosters, self.implants, self.projectedDrones, self.projectedModules, self.projectedFits, (self.character, self.extraAttributes))
        for stuff in c:
            if stuff != None: stuff.clear()


    def calculateModifiedAttributes(self, targetFit = None):
        if targetFit == None:
            targetFit = self
            forceProjected = False
        elif targetFit not in self.__calculatedTargets:
            self.__calculatedTargets.append(targetFit)
            targetFit.calculateModifiedAttributes()
            forceProjected = True
        else:
            return

        if self.__calculated == True and forceProjected == False:
            return
        else:
            self.__calculated = True
        #There's a few things to keep in mind here
        #1: Early effects first, then regular ones, then late ones, regardless of anything else
        #2: Some effects aren't implemented
        #3: Some effects are implemented poorly and will just explode on us
        #4: Errors should be handled gracefully and preferably without crashing unless serious
        for runTime in ("early", "normal", "late"):
            #Lets start out with the ship's effects
            #We'll be ignoring gang/projected effects for now and focussing on regular ones
            extra = []
            if self.character != None:
                extra.append(self.character)
            if self.ship != None:
                extra.append(self.ship)

            c = chain(extra, self.drones, self.boosters, self.implants, self.modules,
                      self.projectedDrones, self.projectedModules)

            for item in c:
                item.calculateModifiedAttributes(targetFit, runTime, forceProjected)


        for fit in self.projectedFits:
            fit.calculateModifiedAttributes(self)

class HandledDroneList(HandledList):
    def __init__(self):
        self.__findCache = {}

    def find(self, item):
        if self.__findCache.has_key(item.ID):
            return self.__findCache[item.ID]
        else:
            return None

    def append(self, drone):
        if self.__findCache.has_key(drone.item.ID):
            raise ValueError("Drone already here, cannot add the same one multiple times")

        HandledList.append(self, drone)
        self.__findCache[drone.item.ID] = drone

    def remove(self, drone):
        if self.__findCache.has_key(drone.item.ID):
            del self.__findCache[drone.item.ID]
            HandledList.remove(self, drone)
        else:
            raise KeyError("Drone is not in the list")

    def appendItem(self, item, amount = 1):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.find(item)
        if d is None:
            d = Drone(item)
            self.append(d)

        d.amount += amount
        return d

    def removeItem(self, item, amount):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.findDrone(item)
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
                else: raise ValueError("Booster/Implant slot already in use, remove the old one first or set replace = True ")

        HandledList.append(self, booster)

class HandledProjectedModList(HandledList):
    def append(self, proj):
        proj.projected = True
        HandledList.append(self, proj)

class HandledProjectedDroneList(HandledDroneList):
    def append(self, proj):
        proj.projected = True
        HandledDroneList.append(self, proj)

class HandledProjectedFitList(list):
    def append(self, proj):
        proj.projected = True
        list.append(self, proj)
from model.types import Drone, Ship, Character
