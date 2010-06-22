from ..item import Item

class Module(object):
    """An instance of this class represents a module together with its ammo and modified attributes"""
    def __init__(self):
        self.__item = None
        self.__ammo = None
        self.__itemModifiedAttributes = {}
        self.__ammoModifiedAttributes = {}
        
    @property
    def item(self):
        return self.__item
    
    @item.setter
    def item(self, item):
        if type(item) != Item and item != None: raise ValueError("Expecting an item, got a " + str(type(item)))
        self.__item = item
        self.__itemModifiedAttributes.clear()
        self.__ammoModifiedAttributes.clear()
        
    @property
    def ammo(self):
        return self.__ammo
    
    @ammo.setter
    def ammo(self, ammo):
        if type(ammo) != Item and ammo != None: raise ValueError("Expecting an item, got a " + str(type(ammo)))
        self.__ammo = ammo
        self.__itemModifiedAttributes.clear()
        self.__ammoModifiedAttributes.clear()