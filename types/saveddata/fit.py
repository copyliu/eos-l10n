from model.types import Character, User
import model.types.saveddata.module
from model.types import Drone
from model.types.gamedata.item import Item
from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict
from sqlalchemy.orm import validates
class Fit(object):
    """Represents a fitting, with modules, ship and character"""
    shipRequiredAttributes = ("cpuOutput", "powerOutput", "rechargeRate", "rigSize", 
                              "scanResolution", "signatureRadius", "hp", "armorHP", "shieldCapacity",
                              "maxVelocity", "agility", "hiSlots", "medSlots", "lowSlots")
    def __init__(self):
        self.__modules = []
        self.__drones = []
        self.__implants = {}
        self.__boosters = {}
        self.__blockedItems = set()
        self.__projectedModules = []
        self.__projectedFits = []
        self.__gang = None
        self.__character = None
        self.__owner = None
        self.__ship = None
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
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, owner):
        self.__owner = owner

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
            
    def addDrone(self, item, amount = 1):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.findDrone(item)
        if d is None:
            d = Drone()
            d.item = item
            
        d.amount += amount
    
    def removeDrone(self, item, amount):
        if amount < 1: ValueError("Amount of drones to add should be >= 1")
        d = self.findDrone(item)
        if d is None:
            d = Drone()
            d.item = item
            
        d.amount -= amount
        
    def iterDrones(self):
        return self.__drones.__iter__()
    
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
                effect.handler(self, self.ship)
            #Handle the rest through their respective classes
            for module in self.iterModules():
                effect.handler(self, module)
            for drone in self.iterDrones():
                pass