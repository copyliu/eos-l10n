from model.types import Character, Module, User
from model.types.gamedata.item import Item
from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict
class Fit(object):
    """Represents a fitting, with modules, ship and character"""
    shipRequiredAttributes = ("cpuOutput", "powerOutput", "rechargeRate", "rigSize", 
                              "scanResolution", "signatureRadius", "hp", "armorHP", "shieldCapacity",
                              "maxVelocity", "agility", "hiSlots", "medSlots", "lowSlots")
    def __init__(self):
        self.__modules = []
        self.__character = None
        self.__owner = None
        self.__ship = None
        self.__shipModifiedAttributes = ModifiedAttributeDict()

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
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, owner):
        if owner == None or type(owner) == User:
            self.__owner = owner
        else:
            raise ValueError("User should be an owner or None, not " + type(owner))
        
    def addModule(self, mod):
        if type(mod) != Module: raise ValueError("Expecting a module to be passed, got " + str(type(mod)))
        self.__modules.append(mod)
        
    def removeModule(self, mod):
        if type(mod) != Module: raise ValueError("Expecting a module to be passed, got " + str(type(mod)))
        self.__modules.remove(mod)
    
    def iterModules(self):
        return self.__modules.__iter__()
    
    