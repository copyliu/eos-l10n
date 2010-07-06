from model.types.saveddata.modifiedAttributeDict import ModifiedAttributeDict

class Implant(object):
    def __init__(self, item):
        self.__slot = self.__calculateSlot(item)
        self.__item = item
        self.__itemModifiedAttributes = ModifiedAttributeDict()
        self.__itemModifiedAttributes.original = item.attributes
    
    @property
    def itemModifiedAttributes(self):
        return self.__itemModifiedAttributes
    
    @property
    def slot(self):
        return self.__slot
    
    @property
    def item(self):
        return self.__item

    def __calculateSlot(self, item):
        if not "implantness" in item.attributes:
            raise ValueError("Passed item is not an implant")
        
        return int(item.attributes["implantness"].value)
    
    def calculateModifiedAttributes(self, fit, runTime):
        for effect in self.item.effects:
            if effect.runTime == runTime:
                effect.handler(fit, self)