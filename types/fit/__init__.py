from ..character import Character
from ..module import Module

class Fit(object):
    """Represents a fitting, with modules and character"""
    def __init__(self):
       self.__modules = []
       self.__character = None

    @property
    def character(self):
        return self.__character;
    
    @character.setter
    def character(self, char):
        if(type(char) != Character and char != None): raise ValueError("Expecting a character or None, got " + str(type(char)))
        self.__character = char
        
    def addModule(self, mod):
        if(type(mod) != Module): raise ValueError("Expecting a module to be passed, got " + str(type(mod)))
        self.__modules.append(mod)
        
    def removeModule(self, mod):
        if(type(mod) != Module): raise ValueError("Expecting a module to be passed, got " + str(type(mod)))
        self.__modules.remove(mod)
    
    def iterModules(self):
        return self.__modules.__iter__()