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

from eos.effectHandlerHelpers import HandledList, HandledModuleList, HandledDroneList, \
HandledImplantBoosterList, HandledProjectedDroneList
from eos.modifiedAttributeDict import ModifiedAttributeDict
from sqlalchemy.orm import validates, reconstructor
from itertools import chain
from eos import capSim
from copy import deepcopy
from math import sqrt, log
from eos.types import Drone, Ship, Character, State, Slot, Module
import re
import xml.dom

class Fit(object):
    """Represents a fitting, with modules, ship, implants, etc."""
    EXTRA_ATTRIBUTES = {"armorRepair": 0,
                        "hullRepair": 0,
                        "shieldRepair": 0,
                        "maxActiveDrones": 0,
                        "maxTargetsLockedFromSkills": 2,
                        "droneControlRange": 0,
                        "capacity": 0,
                        "cloaked": False}

    PEAK_RECHARGE = 0.25

    def __init__(self):
        self.__modules = HandledModuleList()
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

    @classmethod
    def importAuto(cls, string):
        string = string.strip()
        if string[0] == "<":
            return "XML", cls.importXml(string)
        elif string[0] == "[":
            return "EFT", (cls.importEft(string),)
        else:
            return "DNA", (cls.importDna(string),)

    @classmethod
    def importDna(cls, string):
        from eos import db
        info = string.split(":")
        f = Fit()
        f.ship = Ship(db.getItem(int(info[0])))
        f.name = "%s - DNA Imported" % f.ship.item.name
        for itemInfo in info[1:]:
            if itemInfo:
                itemID, amount = itemInfo.split(";")
                item = db.getItem(int(itemID), eager="group.category")

                if item.category.name == "Drone":
                    d = Drone(item)
                    d.amount = int(amount)
                    f.drones.append(d)
                else:
                    m = Module(item)
                    f.modules.append(m)
                    if m.isValidState(State.ACTIVE):
                        m.state = State.ACTIVE

        return f

    typeNameRe = re.compile("\\[(.*), (.*)\\]")

    @classmethod
    def importEft(cls, eftString):
        from eos import db
        fit = cls()
        eftString = eftString.strip()
        lines = re.split('[\n\r]+', eftString)
        shipType, fitName = re.match(cls.typeNameRe, lines[0]).groups()
        try:
            fit.ship = Ship(db.getItem(shipType))
            fit.name = fitName
        except:
            return

        for i in range(1, len(lines)):
            line = lines[i]
            modAmmo = line.split(",")
            modDrone = modAmmo[0].split(" x")
            if len(modAmmo) == 2: ammoName = modAmmo[1].strip()
            else: ammoName = None
            modName = modDrone[0].strip()
            if len(modDrone) == 2: droneAmount = modDrone[1].strip()
            else: droneAmount = None
            try:
                item = db.getItem(modName, eager="group.category")
            except:
                try:
                    item = db.getItem(modAmmo[0], eager="group.category")
                except:
                    continue

            if item.category.name == "Drone":
                droneAmount = int(droneAmount) if droneAmount is not None else 1
                d = Drone(item)
                d.amount = droneAmount
                fit.drones.append(d)
            else:
                m = Module(item)
                if ammoName:
                    m.charge = db.getItem(ammoName)

                if m.isValidState(State.ACTIVE):
                    m.state = State.ACTIVE

                fit.modules.append(m)

        return fit

    @classmethod
    def importXml(cls, text):
        doc = xml.dom.minidom.parseString(text)
        fittings = doc.getElementsByTagName("fittings").item(0)
        fittings = fittings.getElementsByTagName("fitting")
        fits = []
        from eos import db
        for fitting in fittings:
            try:
                f = Fit()
                f.name = fitting.getAttribute("name")
                shipType = fitting.getElementsByTagName("shipType").item(0).getAttribute("value")
                f.ship = Ship(db.getItem(shipType))
                hardwares = fitting.getElementsByTagName("hardware")
                for hardware in hardwares:
                    moduleName = hardware.getAttribute("type")
                    item = db.getItem(moduleName, eager="group.category")
                    if item:
                        if item.group.name == "Drone":
                            d = Drone(item)
                            d.amount = int(hardware.getAttribute("qty"))
                            f.drones.append(d)
                        else:
                            m = Module(item)
                            if m.isValidState(State.ACTIVE):
                                m.state = State.ACTIVE

                            f.modules.append(m)

                fits.append(f)
            except Exception:
                pass

        return fits

    EXPORT_ORDER_EFT = [Slot.SUBSYSTEM, Slot.HIGH, Slot.MED, Slot.LOW, Slot.RIG]
    def exportEft(self):
        export = "[%s, %s]\n" % (self.ship.item.name, self.name)
        stuff = {}
        for module in self.modules:
            slot = module.slot
            if not slot in stuff: stuff[slot] = []
            curr = module.item.name if module.item else ("[Empty %s slot]" % Slot.getName(slot).capitalize() if slot is not None else "")
            if module.charge:
                curr += ", %s" % module.charge.name
            curr += "\n"
            stuff[slot].append(curr)

        for slotType in self.EXPORT_ORDER_EFT:
            data = stuff.get(slotType)
            if data is not None:
                export += "\n"
                for curr in data:
                    export += curr

        export += "\n\n"
        for drone in self.drones:
            export += "%s x%s\n" % (drone.item.name, drone.amount)

        return export

    def exportDna(self):
        dna = str(self.shipID)
        for mod in self.modules:
            if not mod.isEmpty:
                dna += ":%d;1" % mod.itemID

        for drone in self.drones:
            dna += ":%d;%d" % (drone.itemID, drone.amount)

        return dna + "::"

    @classmethod
    def exportXml(cls, *fits):
        doc = xml.dom.minidom.Document()
        fittings = doc.createElement("fittings")
        doc.appendChild(fittings)

        for fit in fits:
            fitting = doc.createElement("fitting")
            fitting.setAttribute("name", fit.name)
            fittings.appendChild(fitting)
            description = doc.createElement("description")
            description.setAttribute("value", "")
            fitting.appendChild(description)
            shipType = doc.createElement("shipType")
            shipType.setAttribute("value", fit.ship.item.name)
            fitting.appendChild(shipType)

            slotNum = {}
            for module in fit.modules:
                if module.isEmpty:
                    continue

                slot = module.slot
                if not slot in slotNum: slotNum[slot] = 0
                slotId = slotNum[slot]
                slotNum[slot] += 1
                hardware = doc.createElement("hardware")
                hardware.setAttribute("type", module.item.name)
                slotName = Slot.getName(slot).lower()
                slotName = slotName if slotName != "high" else "hi"
                hardware.setAttribute("slot", "%s slot %d" % (slotName, slotId))
                fitting.appendChild(hardware)

            for drone in fit.drones:
                hardware = doc.createElement("hardware")
                hardware.setAttribute("qty", "%d" % drone.amount)
                hardware.setAttribute("slot", "drone bay")
                hardware.setAttribute("type", drone.item.name)
                fitting.appendChild(hardware)

        return doc.toprettyxml()

    @reconstructor
    def init(self):
        self.build()

    def build(self):
        from eos import db
        self.__extraDrains = []
        self.__ehp = None
        self.__weaponDPS = None
        self.__weaponVolley = None
        self.__droneDPS = None
        self.__sustainableTank = None
        self.__effectiveSustainableTank = None
        self.__effectiveTank = None
        self.__calculated = False
        self.__capStable = None
        self.__capState = None
        self.__capUsed = None
        self.__capRecharge = None
        self.__calculatedTargets = []
        self.extraAttributes = ModifiedAttributeDict(self)
        self.extraAttributes.original = self.EXTRA_ATTRIBUTES
        self.ship = Ship(db.getItem(self.shipID)) if self.shipID is not None else None

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
        if ship is not None:
            self.extraAttributes["capacity"] = ship.item.capacity

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

    @property
    def maxTargets(self):
        return min(self.extraAttributes["maxTargetsLockedFromSkills"], self.ship.getModifiedItemAttr("maxLockedTargets"))

    @property
    def scanStrength(self):
        return max([self.ship.getModifiedItemAttr("scan%sStrength" % scanType)
                    for scanType in ("Magnetometric", "Ladar", "Radar", "Gravimetric")])

    @property
    def scanType(self):
        type = None
        str = 0
        for scanType in ("Magnetometric", "Ladar", "Radar", "Gravimetric"):
            currStr = self.ship.getModifiedItemAttr("scan%sStrength" % scanType)
            if currStr > str:
                type = scanType
                str = currStr

        return type

    @property
    def alignTime(self):
        agility = self.ship.getModifiedItemAttr("agility")
        mass = self.ship.getModifiedItemAttr("mass")

        return -log(0.25) * agility * mass / 1000000

    @property
    def appliedImplants(self):
        implantsBySlot = {}
        if self.character:
            for implant in self.character.implants:
                implantsBySlot[implant.slot] = implant

        for implant in self.implants:
            implantsBySlot[implant.slot] = implant

        return implantsBySlot.values()

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
        self.__effectiveSustainableTank = None
        self.__sustainableTank = None
        self.__droneDPS = None
        self.__ehp = None
        self.__calculated = False
        self.__capStable = None
        self.__capState = None
        self.__capUsed = None
        self.__capRecharge = None
        del self.__calculatedTargets[:]
        del self.__extraDrains[:]

        if self.ship is not None: self.ship.clear()
        c = chain(self.modules, self.drones, self.boosters, self.implants, self.projectedDrones, self.projectedModules, self.projectedFits, (self.character, self.extraAttributes))
        for stuff in c:
            if stuff is not None: stuff.clear()
        if self.ship is not None:
            self.extraAttributes["capacity"] = self.ship.item.capacity

    #Methods to register and get the thing currently affecting the fit,
    #so we can correctly map "Affected By"
    def register(self, currModifier):
        self.__modifier = currModifier
        if hasattr(currModifier, "itemModifiedAttributes"):
            currModifier.itemModifiedAttributes.fit = self
        if hasattr(currModifier, "chargeModifiedAttributes"):
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
            c = chain((self.character, self.ship), self.drones, self.boosters, self.appliedImplants, self.modules,
                      self.projectedDrones, self.projectedModules)

            for item in c:
                #Registering the item about to affect the fit allows us to track "Affected By" relations correctly
                if item is not None:
                    targetFit.register(item)
                    item.calculateModifiedAttributes(targetFit, runTime, forceProjected)

        for fit in self.projectedFits:
            fit.calculateModifiedAttributes(self)

    def fill(self):
        """
        Fill this fit's module slots with enough dummy slots so that all slots are used.
        This is mostly for making the life of gui's easier.
        GUI's can call fill() and then stop caring about empty slots completely.
        """
        if self.ship is None:
            return

        for slotType in (Slot.LOW, Slot.MED, Slot.HIGH, Slot.RIG, Slot.SUBSYSTEM):
            amount = self.getSlotsFree(slotType, True)
            if amount > 0:
                for _ in xrange(int(amount)):
                    self.modules.append(Module.buildEmpty(slotType))

            if amount < 0:
                #Look for any dummies of that type to remove
                for mod in self.modules:
                    if mod.isEmpty and mod.slot == slotType:
                        self.modules.remove(mod)
                        amount += 1
                        if amount == 0:
                            break

    def getItemAttrSum(self, dict, attr):
        amount = 0
        for mod in dict:
            add = mod.getModifiedItemAttr(attr)
            if add is not None:
                amount += add

        return amount

    def getItemAttrOnlineSum(self, dict, attr):
        amount = 0
        for mod in dict:
            add = mod.getModifiedItemAttr(attr) if mod.state >= State.ONLINE else None
            if add is not None:
                amount += add

        return amount

    def getHardpointsUsed(self, type):
        amount = 0
        for mod in self.modules:
            if mod.hardpoint is type and not mod.isEmpty:
                amount += 1

        return amount

    def getSlotsUsed(self, type, countDummies=False):
        amount = 0
        for mod in self.modules:
            if mod.slot is type and (not mod.isEmpty or countDummies):
                amount += 1

        return amount

    def getSlotsFree(self, type, countDummies=False):
        slots = {Slot.LOW: "lowSlots",
                 Slot.MED: "medSlots",
                 Slot.HIGH: "hiSlots",
                 Slot.RIG: "rigSlots",
                 Slot.SUBSYSTEM: "maxSubSystems"}

        slotsUsed = self.getSlotsUsed(type, countDummies)
        totalSlots = self.ship.getModifiedItemAttr(slots[type]) or 0
        return totalSlots - slotsUsed

    @property
    def calibrationUsed(self):
        return self.getItemAttrSum(self.modules, 'upgradeCost')

    @property
    def pgUsed(self):
        return self.getItemAttrOnlineSum(self.modules, "power")

    @property
    def cpuUsed(self):
        return self.getItemAttrOnlineSum(self.modules, "cpu")

    @property
    def droneBandwidthUsed(self):
        amount = 0
        for d in self.drones:
            amount += d.getModifiedItemAttr("droneBandwidthUsed") * d.amountActive

        return amount

    @property
    def droneBayUsed(self):
        amount = 0
        for d in self.drones:
            amount += d.item.volume * d.amount

        return amount


    @property
    def capStable(self):
        if self.__capStable is None:
            self.simulateCap()

        return self.__capStable

    @property
    def capState(self):
        """
        If the cap is stable, the capacitor state is the % at which it is stable.
        If the cap is unstable, this is the amount of time before it runs out
        """
        if self.__capState is None:
            self.simulateCap()

        return self.__capState

    @property
    def capUsed(self):
        if self.__capUsed is None:
            self.simulateCap()

        return self.__capUsed

    @property
    def capRecharge(self):
        if self.__capRecharge is None:
            self.simulateCap()

        return self.__capRecharge


    @property
    def sustainableTank(self):
        if self.__sustainableTank is None:
            self.calculateSustainableTank()

        return self.__sustainableTank

    def calculateSustainableTank(self, effective=True):
        if self.__sustainableTank is None:
            if self.capStable:
                sustainable = {}
                sustainable["armorRepair"] = self.extraAttributes["armorRepair"]
                sustainable["shieldRepair"] = self.extraAttributes["shieldRepair"]
                sustainable["hullRepair"] = self.extraAttributes["hullRepair"]
            else:
                sustainable = {}

                repairers = []
                #Map a repairer type to the attribute it uses
                groupAttrMap = {"Armor Repair Unit": "armorDamageAmount",
                     "Hull Repair Unit": "structureDamageAmount",
                     "Shield Booster": "shieldBonus"}
                #Map repairer type to attribute
                groupStoreMap = {"Armor Repair Unit": "armorRepair",
                                 "Hull Repair Unit": "hullRepair",
                                 "Shield Booster": "shieldRepair"}

                capUsed = self.capUsed
                for attr in ("shieldRepair", "armorRepair", "hullRepair"):
                    sustainable[attr] = self.extraAttributes[attr]
                    dict = self.extraAttributes.getAfflictions(attr)
                    if self in dict:
                        for mod, _, amount in dict[self]:
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
                totalPeakRecharge = self.capRecharge
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

            sustainable["passiveShield"] = self.calculateShieldRecharge()
            self.__sustainableTank = sustainable

        return self.__sustainableTank

    def calculateCapRecharge(self, percent = PEAK_RECHARGE):
        capacity = self.ship.getModifiedItemAttr("capacitorCapacity")
        rechargeRate = self.ship.getModifiedItemAttr("rechargeRate") / 1000.0
        return 10 / rechargeRate * sqrt(percent) * (1 - sqrt(percent)) * capacity

    def calculateShieldRecharge(self, percent = PEAK_RECHARGE):
        capacity = self.ship.getModifiedItemAttr("shieldCapacity")
        rechargeRate = self.ship.getModifiedItemAttr("shieldRechargeRate") / 1000.0
        return 10 / rechargeRate * sqrt(percent) * (1 - sqrt(percent)) * capacity

    def addDrain(self, cycleTime, capNeed, clipSize=0):
        self.__extraDrains.append((cycleTime, capNeed, clipSize))

    def removeDrain(self, i):
        del self.__extraDrains[i]

    def iterDrains(self):
        return self.__extraDrains.__iter__()

    def __generateDrain(self):
        drains = []
        capUsed = 0
        capAdded = 0
        for mod in self.modules:
            if mod.state == State.ACTIVE:
                capNeed = mod.getModifiedItemAttr("capacitorNeed")
                if capNeed != 0 and capNeed is not None:
                    cycleTime = mod.getCycleTime()
                    if capNeed > 0:
                        capUsed += capNeed / cycleTime
                    else:
                        capAdded += -capNeed / cycleTime

                    drains.append((int(cycleTime * 1000), capNeed, mod.numCharges))

        for cycleTime, capNeed, clipSize in self.iterDrains():
            drains.append((int(cycleTime * 1000), capNeed, clipSize))
            if capNeed > 0:
                capUsed += capNeed / cycleTime
            else:
                capAdded += -capNeed / cycleTime

        return drains, capUsed, capAdded

    def simulateCap(self):
        drains, self.__capUsed, self.__capRecharge = self.__generateDrain()
        self.__capRecharge += self.calculateCapRecharge()
        if len(drains) > 0:
            sim = capSim.CapSimulator()
            sim.init(drains)
            sim.capacitorCapacity = self.ship.getModifiedItemAttr("capacitorCapacity")
            sim.capacitorRecharge = self.ship.getModifiedItemAttr("rechargeRate")
            sim.stagger = True
            sim.scale = False
            sim.reload = False
            sim.run()

            self.__capStable = sim.cap_stable_eve > 0
            self.__capState = min(100, sim.cap_stable_eve * 100) if self.__capStable else sim.t / 1000.0
        else:
            self.__capStable = True
            self.__capState = 100

    @property
    def hp(self):
        hp = {}
        for (type, attr) in (('shield', 'shieldCapacity'), ('armor', 'armorHP'), ('hull', 'hp')):
            hp[type] = self.ship.getModifiedItemAttr(attr)

        return hp

    @property
    def ehp(self):
        if self.__ehp is None:
            if self.damagePattern is None:
                ehp = self.hp
            else:
                ehp = self.damagePattern.calculateEhp(self)
            self.__ehp = ehp
        return self.__ehp

    @property
    def tank(self):
        hps = {"passiveShield" : self.calculateShieldRecharge()}
        for type in ("shield", "armor", "hull"):
            hps["%sRepair" % type] = self.extraAttributes["%sRepair" % type]

        return hps

    @property
    def effectiveTank(self):
        if self.__effectiveTank is None:
            if self.damagePattern is None:
                ehps = self.hps
            else:
                ehps = self.damagePattern.calculateEffectiveTank(self, self.extraAttributes)

            self.__effectiveTank = ehps

        return self.__effectiveTank

    @property
    def effectiveSustainableTank(self):
        if self.__effectiveSustainableTank is None:
            if self.damagePattern is None:
                eshps = self.sustainableTank
            else:
                eshps = self.damagePattern.calculateEffectiveTank(self, self.sustainableTank)

            self.__effectiveSustainableTank = eshps

        return self.__effectiveSustainableTank

    def calculateWeaponStats(self):
        weaponDPS = 0
        droneDPS = 0
        weaponVolley = 0

        for mod in self.modules:
            dps, volley = mod.damageStats
            weaponDPS += dps
            weaponVolley += volley

        for drone in self.drones:
            droneDPS += drone.dps

        self.__weaponDPS = weaponDPS
        self.__weaponVolley = weaponVolley
        self.__droneDPS = droneDPS

    def __deepcopy__(self, memo):
        copy = Fit()
        #Character and owner are not copied
        copy.character = self.__character
        copy.owner = self.owner
        copy.ship = deepcopy(self.ship, memo)
        copy.name = "%s copy" % self.name
        copy.damagePattern = self.damagePattern

        toCopy = ("modules", "drones", "implants", "boosters", "projectedModules", "projectedDrones")
        for name in toCopy:
            orig = getattr(self, name)
            c = getattr(copy, name)
            for i in orig:
                c.append(deepcopy(i, memo))

        for fit in self.projectedFits:
            copy.projectedFits.append(fit)

        return copy
