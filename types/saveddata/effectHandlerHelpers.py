class HandledList(object):
    def __init__(self):
        self.__list = []
        
    def __getitem__(self, key):
        return self.__list[key]
    
    def __setitem(self, key, val):
        self.__list[key] = val
    
    def __iter__(self):
        return self.__list.__iter__()
    
    iter = __iter__
    
    def append(self, val):
        return self.__list.append(val)
        
    def remove(self, val):
        return self.__list.remove(val)
    
    def increaseAllItems(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.increaseItem(*args, **kwargs)
                
    def multiplyAllItems(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.multiplyItem(*args, **kwargs)
                
    def boostAllItems(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.boostItem(*args, **kwargs)
                
    def increaseAllCharges(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.increaseCharge(*args, **kwargs)
                
    def multiplyAllCharges(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.multiplyCharge(*args, **kwargs)
                
    def boostAllCharges(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.boostCharge(*args, **kwargs)

class HandledItem(object):
    def increaseItemAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.increase(*args, **kwargs)
    
    def multiplyItemAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.multiply(*args, **kwargs)
        
    def boostItemAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.boost(*args, **kwargs)
        
class HandledCharge(object):
    def increaseChargeAttr(self, *args, **kwargs):
        self.chargeModifiedAttributes.increase(*args, **kwargs)
        
    def multiplyChargeAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.multiply(*args, **kwargs)
        
    def boostChargeAttr(self, *args, **kwargs):
        self.itemModifiedAttributes.boost(*args, **kwargs)