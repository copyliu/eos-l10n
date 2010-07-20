from model.types import Drone
from model.effectHandlerHelpers import HandledSet
from model.modifiedAttributeDict import ModifiedAttributeDict
from sqlalchemy.orm import validates, reconstructor
from itertools import chain

class Fit(object):
    """Represents a fitting, with modules, ship, implants, etc."""
    
    def __init__(self):
        self.__modules = HandledSet()
        self.__drones = HandledDroneSet()
        self.__implants = HandledImplantBoosterSet()
        self.__boosters = HandledImplantBoosterSet()
        self.__blockedItems = set()
        self.__projectedModules = HandledSet()
        self.__projectedFits = HandledSet()
        self.__gang = None
        self.__character = None
        self.__owner = None
        self.shipID = None
        self.name = ""
        self.build()
        
    @reconstructor
    def init(self):
        self.build()
    
    def build(self):
        from model import db
        self.__ship = db.getItem(self.shipID) if self.shipID != None else None
        self.__shipModifiedAttributes = ModifiedAttributeDict()
        self.clear()
        
    @property
    def shipModifiedAttributes(self):
        return self.__shipModifiedAttributes
    
    @property
    def character(self):
        return self.__character;
    
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
    
    @validates("ID", "ownerID", "shipID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "ownerID" : lambda val: isinstance(val, int),
               "shipID" : lambda val: isinstance(val, int) or val == None}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
    
    def clear(self):
        self.ship.clear()
        chain = chain(self.modules, self.drones, self.boosters, self.implants, (self.character,))
        for stuff in chain: stuff.clear()
        self.armorRepair, self.droneControlRange, self.shieldRepair, self.hullRepair, self.extraCapRecharge, self.maxActiveDrones = 0, 0, 0, 0, 0, 0
        self.cloaked = False
    
    def calculateModifiedAttributes(self):
        #There's a few things to keep in mind here
        #1: Early effects first, then regular ones, then late ones, regardless of anything else
        #2: Some effects aren't implemented
        #3: Some effects are implemented poorly and will just explode on us
        #4: Errors should be handled gracefully and preferably without crashing unless serious
        for runTime in ("early", "normal", "late"):
            #Lets start out with the ship's effects
            #We'll be ignoring gang/projected effects for now and focussing on regular ones
            self.character.calculateModifiedAttributes(self, runTime)
            self.ship.calculateModifiedAttributes(self, runTime)
            #Handle the rest through their respective classes
            for drone in self.drones: drone.calculateModifiedAttributes(self, runTime)
            for booster in self.boosters: booster.calculateModifiedAttributes(self, runTime)
            for implant in self.implants: implant.calculateModifiedAttributes(self, runTime)
            for module in self.modules: module.calculateModifiedAttributes(self, runTime)
    
class HandledDroneSet(HandledSet):
    def __init__(self):
        self.__findCache = {}
    
    def find(self, item):
        if self.__findCache.has_key(item.ID):
            return self.__findCache[item.ID]
        else:
            return None
        
    def add(self, drone):
        if self.__findCache.has_key(drone.item.ID):
            raise ValueError("Drone already here, cannot add the same one multiple times")
        
        set.add(self, drone)
        self.__findCache[drone.item.ID] = drone
    
    def remove(self, drone):
        if self.__findCache.has_key(drone.item.ID):
            del self.__findCache[drone.item.ID]
        else:
            raise KeyError("Drone is not in the list")
        
    def addItem(self, item, amount = 1):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.find(item)
        if d is None:
            d = Drone(item)
            self.add(d)
            
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
    
class HandledImplantBoosterSet(HandledSet):
    def __init__(self):
        self.__slotCache = {}
        
    def add(self, booster, replace = False):
        if self.__slotCache.has_key(booster.slot):
            if replace: self.remove(booster)
            else: 
                if replace: self.remove(booster)
                else: raise ValueError("Booster/Implant slot already in use, remove the old one first or set replace = True ")
        
        set.add(self, booster)