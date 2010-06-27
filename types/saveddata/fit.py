from character import Character
from ..gamedata.item import Item
from module import Module
from modifiedAttributeDict import ModifiedAttributeDict
class Fit(object):
    """Represents a fitting, with modules, ship and character"""
    shipRequiredAttributes = ("cpuOutput", "powerOutput", "rechargeRate", "rigSize", 
                              "scanResolution", "signatureRadius", "hp", "armorHP", "shieldCapacity",
                              "maxVelocity", "agility", "hiSlots", "medSlots", "lowSlots")
    def __init__(self):
       self.__modules = []
       self.__character = None
       self.__ship = None
       self.__shipModifiedAttributes = {}

    @property
    def character(self):
        return self.__character;
    
    @character.setter
    def character(self, char):
        if type(char) != Character and char != None: raise ValueError("Expecting a character or None, got " + str(type(char)))
        self.__character = char
    
    @property
    def ship(self):
        return self.__ship
    
    @ship.setter
    def ship(self, ship):
        if ship != None:
            if type(ship) != Item: raise ValueError("Expecting an item to be passed, got " + str(type(ship)))
            #We NEED a few attributes for ships when calculating stuff, make sure they're there
            for requiredAttr in self.shipRequiredAttributes:
                if not requiredAttr in  ship.attributes:
                    raise ValueError("Passed item is not a ship")
        
        self.__ship = ship
        self.__shipModifiedAttributes.clear()
            
    def addModule(self, mod):
        if type(mod) != Module: raise ValueError("Expecting a module to be passed, got " + str(type(mod)))
        self.__modules.append(mod)
        
    def removeModule(self, mod):
        if type(mod) != Module: raise ValueError("Expecting a module to be passed, got " + str(type(mod)))
        self.__modules.remove(mod)
    
    def iterModules(self):
        return self.__modules.__iter__()
    
    