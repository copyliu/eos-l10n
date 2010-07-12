from model.types import Drone
from model.effectHandlerHelpers import HandledList
from model.modifiedAttributeDict import ModifiedAttributeDict
from sqlalchemy.orm import validates, reconstructor

class Fit(object):
    """Represents a fitting, with modules, ship and character"""
    shipRequiredAttributes = ("cpuOutput", "powerOutput", "rechargeRate", "rigSize", 
                              "scanResolution", "signatureRadius", "hp", "armorHP", "shieldCapacity",
                              "maxVelocity", "agility", "hiSlots", "medSlots", "lowSlots")
    def __init__(self):
        self.__modules = HandledList()
        self.__drones = HandledList()
        self.__implants = HandledList()
        self.__boosters = HandledList()
        self.__blockedItems = set()
        self.__projectedModules = HandledList()
        self.__projectedFits = HandledList()
        self.__gang = None
        self.__character = None
        self.__owner = None
        self.shipID = None
        self.name = ""
    
    @reconstructor
    def init(self):
        self.build()
    
    def build(self):
        from model import db
        self.__ship = db.getItem(self.shipID) if self.shipID != None else None
        self.__shipModifiedAttributes = ModifiedAttributeDict()
    
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
        if ship != None:
            #We NEED a few attributes for ships when calculating stuff, make sure they're there
            for requiredAttr in self.shipRequiredAttributes:
                if not requiredAttr in  ship.attributes:
                    raise ValueError("Passed item is not a ship")
        
        self.__ship = ship
        self.shipID = ship.ID if ship != None else None
        self.__shipModifiedAttributes.original = ship.attributes
    
    def getModifiedShipAttr(self, key):
        if key in self.shipModifiedAttributes:
            return self.shipModifiedAttributes[key]
        else:
            return None
        
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
    
    def addModule(self, mod):
        self.__modules.append(mod)
        
    def removeModule(self, mod):
        self.__modules.remove(mod)
    
    def iterModules(self):
        return self.__modules.__iter__()
    
    def findDrone(self, item):
        for d in self.__drones:
            if d.item == item:
                return d
            
    def addDroneItemAmount(self, item, amount = 1):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.findDrone(item)
        if d is None:
            d = Drone(item)
            self.__drones.append(d)
            
        d.amount += amount
        return d
    
    def removeDroneItemAmount(self, item, amount):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.findDrone(item)
        if d is None:
            d = Drone()
            d.item = item
            
        d.amount -= amount
        if d.amount <= 0:
            self.__drones.remove(d)
            return None
        
        return d
    
    def addBooster(self, booster, replace = False):
        for b in self.drones:
            if booster.slot == b.slot:
                if replace: self.removeBooster(b)
                else:
                    raise ValueError("Booster slot already in use, remove the old one first or set replace = True ")
        
        self.__boosters.append(booster)
    
    def removeBooster(self, booster):
        self.__boosters.remove(booster)

    def addImplant(self, implant, replace = False):
        for i in self.iterImplants():
            if implant.slot == i.slot:
                if replace: self.removeImplant(i)
                else:
                    raise ValueError("Implant slot already in use, remove the old one first or set replace to True")
        
        self.__implants.append(implant)
        
    def removeImplant(self, implant):
        self.__implants.remove(implant)
        
    def iterImplants(self):
        return self.__implants.__iter__()
    
    @validates("ID", "ownerID", "shipID")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "ownerID" : lambda val: isinstance(val, int),
               "shipID" : lambda val: isinstance(val, int)}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
    
    def calculateModifiedAttributes(self):
        #There's a few things to keep in mind here
        #1: Early effects first, then regular ones, then late ones, regardless of anything else
        #2: Some effects aren't implemented
        #3: Some effects are implemented poorly and will just explode on us
        #4: Errors should be handled gracefully and preferably without crashing unless serious
        for runTime in ("early", "normal", "late"):
            #Lets start out with the ship's effects
            #We'll be ignoring gang/projected effects for now and focussing on regular ones
            for effect in self.ship.effects:
                if effect.runTime == runTime:
                    effect.handler(self, self.ship)
            #Handle the rest through their respective classes
            for module in self.iterModules(): module.calculateModifiedAttributes(self, runTime)
            for drone in self.iterDrones(): drone.calculateModifiedAttributes(self, runTime)
            for booster in self.iterBoosters(): booster.calculateModifiedAttributes(self, runTime)
            for implant in self.iterImplants(): implant.calculateModifiedAttributes(self, runTime)
            self.character.calculateModifiedAttributes(self, runTime)