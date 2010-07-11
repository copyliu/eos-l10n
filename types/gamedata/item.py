class Item(object):
    def getAttribute(self, key):
        if key in self.attributes:
            return self.attributes[key].value
        
    def isType(self, type):
        for effect in self.effects.itervalues():
            if effect.isType(type):
                return True
        
        return False