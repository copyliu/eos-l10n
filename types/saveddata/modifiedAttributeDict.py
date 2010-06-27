from sqlalchemy.orm.collections import MappedCollection

class ModifiedAttributeDict(object):
    def __init__(self):
        self.__modified = {}
        self.__original = None
        
    def clear(self):
        self.__modified.clear()
        self.__original = None
    
    @property
    def original(self):
        return self.__original
    
    @original.setter
    def original(self, val):
        if val != None and type(val) != MappedCollection: raise ValueError("original was not a valid MappedCollection of attributes")
        self.__original = val
        self.__modified.clear()
        
    def __getitem__(self, key):
        if key in self.__modified: return self.__modified[key]
        else: return self.__original[key].value
    
    def __setitem__(self, key, val):
        self.__modified[key] = val
    
    def __iter__(self):
        all = dict(self.__original, **self.__modified)
        return (key for key in all)
    
    def iterkeys(self):
        for key in self:
            yield key
    
    def itervalues(self):
        for key in self:
            yield self[key]
    
    def iteritems(self):
        for key in self:
            yield key, self[key]