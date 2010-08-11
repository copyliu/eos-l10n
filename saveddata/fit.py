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

from model.effectHandlerHelpers import HandledList
from model.modifiedAttributeDict import ModifiedAttributeDict
from sqlalchemy.orm import validates, reconstructor
from itertools import chain, count
from copy import deepcopy
from math import sqrt, pi, exp
from model.solverMath import gaussian, solve
from model.types import Drone, Ship, Character, State, Hardpoint

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

    PEAK_RECHARGE = -(sqrt(2) - 2 ) / 2

    def __init__(self):
        self.__modules = HandledList()
        self.__drones = HandledDroneList()
        self.__implants = HandledImplantBoosterList()
        self.__boosters = HandledImplantBoosterList()
        self.__projectedModules = HandledList()
        self.__projectedFits = HandledList()
        self.__projectedDrones = HandledProjectedDroneList()
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
        self.__ehp = None
        self.__weaponDPS = None
        self.__weaponVolley = None
        self.__droneDPS = None
        self.__sustainableTank = None
        self.__effectiveTank = None
        self.__calculated = False
        self.__capStable = None
        self.__capState = None
        self.__capUsed = None
        self.__capRecharge = None
        self.__calculatedTargets = []
        self.__ship = Ship(db.getItem(self.shipID)) if self.shipID is not None else None
        self.extraAttributes = ModifiedAttributeDict(self)
        self.extraAttributes.original = self.EXTRA_ATTRIBUTES

    @property
    def damagePattern(self):
        return self.__damagePattern

    @damagePattern.setter
    def damagePattern(self, damagePattern):
        self.__damagePattern = damagePattern
        self.__ehp = None
        self.__effectiveTank = None

    @property
    def character(self):
        return self.__character if self.__character is not None else Character.getAll0()

    @character.setter
    def character(self, char):
        self.__character = char

    @property
    def ship(self):
        return self.__ship

    @ship.setter
    def ship(self, ship):
        self.__ship = ship
        self.shipID = ship.item.ID if ship is not None else None

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

    @property
    def weaponDPS(self):
        if self.__weaponDPS is None:
            self.calculateWeaponStats()

        return self.__weaponDPS

    @property
    def weaponVolley(self):
        if self.__weaponVolley is None:
            self.calculateWeaponStats()

        return self.__weaponVolley

    @property
    def droneDPS(self):
        if self.__droneDPS is None:
            self.calculateWeaponStats()

        return self.__droneDPS

    @property
    def totalDPS(self):
        return self.droneDPS + self.weaponDPS

    @validates("ID", "ownerID", "shipID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "ownerID" : lambda val: isinstance(val, int),
               "shipID" : lambda val: isinstance(val, int) or val is None}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val

    def clear(self):
        self.__effectiveTank = None
        self.__weaponDPS = None
        self.__weaponVolley = None
        self.__droneDPS = None
        self.__ehp = None
        self.__calculated = False
        self.__capStable = None
        self.__capState = None
        self.__capUsed = None
        self.__capRecharge = None
        del self.__calculatedTargets[:]
        if self.ship is not None: self.ship.clear()
        c = chain(self.modules, self.drones, self.boosters, self.implants, self.projectedDrones, self.projectedModules, self.projectedFits, (self.character, self.extraAttributes))
        for stuff in c:
            if stuff is not None: stuff.clear()

    #Methods to register and get the thing currently affecting the fit,
    #so we can correctly map "Affected By"
    def __register(self, currModifier):
        self.__modifier = currModifier
        if hasattr(self, "itemModifiedAttributes"):
            currModifier.itemModifiedAttributes.fit = self
        if hasattr(self, "chargeModifiedAttributes"):
            currModifier.chargeModifiedAttributes.fit = self

    def getModifier(self):
        return self.__modifier

    def calculateModifiedAttributes(self, targetFit = None):
        if targetFit is None:
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
            #Build a little chain of stuff
            c = chain((self.character, self.ship), self.drones, self.boosters, self.implants, self.modules,
                      self.projectedDrones, self.projectedModules)

            for item in c:
                #Registering the item about to affect the fit allows us to track "Affected By" relations correctly
                if item is not None:
                    targetFit.__register(item)
                    item.calculateModifiedAttributes(targetFit, runTime, forceProjected)

        for fit in self.projectedFits:
            fit.calculateModifiedAttributes(self)

    def getHardpointsUsed(self, type):
        amount = 0
        for mod in self.modules:
            if mod.hardpoint is type:
                amount += 1

        return amount

    def calculateCapRecharge(self, percent = PEAK_RECHARGE):
        capacity = self.ship.getModifiedItemAttr("capacitorCapacity")
        rechargeRate = self.ship.getModifiedItemAttr("rechargeRate") / 1000.0
        return capacity * ((4.9678 / rechargeRate) * (1 - percent) *
                           sqrt((2 * percent) - percent ** 2))

    def calculateCapRechargeAbs(self, currCapacity):
        capacity = self.ship.getModifiedItemAttr("capacitorCapacity")
        percent = currCapacity / capacity
        rechargeRate = self.ship.getModifiedItemAttr("rechargeRate") / 1000.0
        return capacity * ((4.9678 / rechargeRate) * (1 - percent) *
                           sqrt((2 * percent) - percent ** 2))

    def calculateShieldRecharge(self, percent = PEAK_RECHARGE):
        capacity = self.ship.getModifiedItemAttr("shieldCapacity")
        rechargeRate = self.ship.getModifiedItemAttr("shieldRechargeRate") / 1000.0
        return capacity * ((4.9678 / rechargeRate) * (1 - percent) *
                           sqrt((2 * percent) - pow(percent, 2)))

    def isCapStable(self):
        if self.__capStable is None:
            self.simulateCap()

        return self.__capStable

    def capState(self):
        """
        If the cap is stable, the capacitor state is the % at which it is stable.
        If the cap is unstable, this is the amount of time before it runs out
        """
        if self.__capState is None:
            self.simulateCap()

        return self.__capState

    def capUsed(self):
        if self.__capUsed is None:
            self.simulateCap()

        return self.__capUsed

    def capRecharge(self):
        if self.__capRecharge is None:
            self.simulateCap()

        return self.__capRecharge

    def __generateDrain(self, variance):
        def mapper(mod):
            cycleTime = mod.getCycleTime()
            drain = mod.getModifiedItemAttr("capacitorNeed")
            def gauss(t):
                return drain * gaussian(cycleTime / 2.0, variance)(t)

            return (cycleTime, gauss)

        mods = filter(lambda mod: mod.getModifiedItemAttr("capacitorNeed") is not None, self.modules)
        drains = map(mapper, mods)
        def result(t):
            m = map(lambda x: x[1](t % x[0]), drains)
            return sum(m)

        return result

    def calculateSustainableTank(self):
        if self.__sustainableTank is None:
            if self.isCapStable():
                sustainable = {}
                sustainable["armorRepair"] = self.extraAttributes["armorRepair"]
                sustainable["shieldRepair"] = self.extraAttributes["shieldRepair"]
                sustainable["hullRepair"] = self.extraAttributes["hullRepair"]
            else:
                sustainable = {}

                groups = ("Armor Repair Unit", "Hull Repair Unit", "Shield Booster")
                repairers = []
                extraRep = {}
                #Map a repairer type to the attribute it uses
                groupAttrMap = {"Armor Repair Unit": "armorDamageAmount",
                     "Hull Repair Unit": "structureDamageAmount",
                     "Shield Booster": "shieldBonus"}
                #Map repairer type to attribute
                groupStoreMap = {"Armor Repair Unit": "armorRepair",
                                 "Hull Repair Unit": "hullRepair",
                                 "Shield Booster": "shieldRepair"}

                capUsed = self.capUsed()
                for attr in ("shieldRepair", "armorRepair", "hullRepair"):
                    sustainable[attr] = self.extraAttributes[attr]
                    dict = self.extraAttributes.getAfflictions(attr)
                    if self in dict:
                        for mod in dict[self]:
                            capUsed -= mod.getCapUsage()
                            cycleTime = mod.getModifiedItemAttr("duration") / 1000.0
                            amount = mod.getModifiedItemAttr(groupAttrMap[mod.item.group.name])
                            sustainable[attr] -= amount / cycleTime
                            repairers.append(mod)

                #Sort repairers by efficiency. We want to use the most efficient repairers first
                repairers.sort(key=lambda mod: mod.getModifiedItemAttr(groupAttrMap[mod.item.group.name]) / mod.getModifiedItemAttr("capacitorNeed"), reverse = True)

                #Loop through every module until we're above peak recharge
                #Most efficient first, as we sorted earlier.
                #calculate how much the repper can rep stability & add to total
                totalPeakRecharge = self.capRecharge()
                for mod in repairers:
                    if capUsed > totalPeakRecharge: break
                    cycleTime = mod.getCycleTime()
                    capPerSec = mod.getCapUsage()
                    if capPerSec is not None and cycleTime is not None:
                        #Check how much this repper can work
                        sustainability = min(1, (totalPeakRecharge - capUsed) / capPerSec)

                        #Add the sustainable amount
                        amount = mod.getModifiedItemAttr(groupAttrMap[mod.item.group.name])
                        sustainable[groupStoreMap[mod.item.group.name]] += sustainability * (amount / cycleTime)
                        capUsed += capPerSec


            self.__sustainableTank = sustainable

        return self.__sustainableTank

    def simulateCap(self):
        #Figure out natural recharge is, boosted amount & drained amount.
        #Compute the total afterwards
        peakRecharge = self.calculateCapRecharge(self.PEAK_RECHARGE)
        capBoost = self.extraAttributes["capBoost"]
        capDrain = self.extraAttributes["capDrain"]
        totalPeakLoad = peakRecharge + capBoost
        self.__capRecharge = totalPeakLoad

        #Figure out how much cap we're using
        capUse = capDrain
        for mod in self.modules:
            if mod.state >= State.ACTIVE:
                capNeed = mod.getModifiedItemAttr("capacitorNeed")
                cycleTime = mod.getModifiedItemAttr("speed") or mod.getModifiedItemAttr("duration")
                if capNeed is not None and cycleTime is not None:
                    capUse += capNeed / (cycleTime / 1000.0)

        self.__capUsed = capUse
        if totalPeakLoad > capUse:
            #Stable!
            #We'll figure out where exactly its stable then.
            #This is rather easy.
            #lower bound = peak recharge
            #Upper bound = 100%
            #We need to find out at how many % capUse == capRecharge
            #Algorithm: keep taking the average between low and up. Call it mid
            #If our recharge at mid % is above our cap use, the mid becomes the new upper bound.
            #If our recharge at mid % is under our cap use, mid becomes new lower bound.
            #Note: This is a variant of binary search.
            low = self.PEAK_RECHARGE
            high = 1.0
            diff = 10
            while diff >= 0.000001:
                mid = (low + high) / 2
                rechargeRate = self.calculateCapRecharge(mid) + capBoost
                diff = abs(rechargeRate - capUse)
                if rechargeRate > capUse:
                    low = mid
                else:
                    high = mid
            self.__capStable = True
            self.__capState = mid * 100
        else:
            VARIANCE = 0.1
            capCapacity = self.ship.getModifiedItemAttr("capacitorCapacity")
            currentCap = capCapacity
            #Solve the cap stuff by integrating and solving it
            r = self.calculateCapRechargeAbs
            d = self.__generateDrain(VARIANCE)
            f_prime = lambda t, y: r(y) - d(t)
            self.__capStable = False
            self.__capState = solve(f_prime, capCapacity)

    def getEhp(self):
        if self.__ehp is None:
            if self.damagePattern is None:
                ehp = {}
                for (type, attr) in (('shield', 'shieldCapacity'), ('armor', 'armorHP'), ('hull', 'hp')):
                    ehp[type] = self.ship.getModifiedItemAttr(attr)
            else:
                ehp = self.damagePattern.calculateEhp(self)
            self.__ehp = ehp
        return self.__ehp

    def getEffectiveTank(self):
        if self.__effectiveTank is None:
            if self.damagePattern is None:
                ehps = {"passiveShield" : self.calculateShieldRecharge()}
                for type in ("shield", "armor", "hull"):
                    ehps[type] = self.extraAttributes["%sRepair" % type]
            else:
                ehps = self.damagePattern.calculateEffectiveTank(self)

            self.__effectiveTank = ehps

        return self.__effectiveTank

    def calculateWeaponStats(self):
        weaponDPS = 0
        droneDPS = 0
        weaponVolley = 0
        damageAttributes = ("emDamage", "kineticDamage", "explosiveDamage", "thermalDamage")
        for mod in self.modules:
            if mod.state == State.ACTIVE and \
            (mod.hardpoint == Hardpoint.TURRET or mod.hardpoint == Hardpoint.MISSILE):
                cycleTime = mod.getCycleTime()
                volley = sum(map(lambda attr: mod.getModifiedChargeAttr(attr), damageAttributes))
                volley *= mod.getModifiedItemAttr("damageMultiplier") or 1
                weaponVolley += volley
                weaponDPS += volley / cycleTime

        for drone in self.drones:
            if drone.active and drone.dealsDamage():
                if drone.hasAmmo():
                    attr = "missileLaunchDuration"
                    getter = drone.getModifiedChargeAttr
                else:
                    attr =  "speed"
                    getter = drone.getModifiedItemAttr

                cycleTime = drone.getModifiedItemAttr(attr) / 1000.0
                volley = sum(map(lambda d: getter(d), damageAttributes)) * drone.amount
                volley *= drone.getModifiedItemAttr("damageMultiplier") or 1
                droneDPS += volley / cycleTime

        self.__weaponDPS = weaponDPS
        self.__weaponVolley = weaponVolley
        self.__droneDPS = droneDPS

    def __deepcopy__(self, memo):
        copy = Fit()
        #Character and owner are not copied
        copy.character = self.character
        copy.owner = self.owner
        copy.ship = deepcopy(self.ship, memo)
        copy.name = "%s copy" % self.name

        toCopy = ("modules", "drones", "implants", "boosters", "projectedModules", "projectedDrones")
        for name in toCopy:
            orig = getattr(self, name)
            c = getattr(copy, name)
            for i in orig:
                c.append(deepcopy(i, memo))

        for fit in self.projectedFits:
            copy.projectedFits.append(fit)

        return copy

class HandledModuleList(HandledList):
    def append(self, mod):
        l = len(self)
        mod.position = l
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
        i = oldPos
        while i < len(self):
            self[i].position -= 1
            i += 1

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
                else: raise ValueError("Booster/Implant slot already in use, remove the old one first or set replace = True")

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
    """
    Use list here, handledList kills sqlalchemy for some unknown reason.
    """
    def append(self, proj):
        proj.projected = True
        list.append(self, proj)
