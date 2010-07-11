class HandledList(list):    
    def filteredItemIncrease(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.increaseItemAttr(*args, **kwargs)
                
    def filteredItemMultiply(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.multiplyItemAttr(*args, **kwargs)
                
    def filteredItemBoost(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.boostItemAttr(*args, **kwargs)
                
    def filteredChargeIncrease(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.increaseChargeAttr(*args, **kwargs)
                
    def filteredChargeMultiply(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.multiplyChargeAttr(*args, **kwargs)
                
    def filteredChargeBoost(self, filter, *args, **kwargs):
        for element in self:
            if filter(element):
                element.boostChargeAttr(*args, **kwargs)

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
        self.chargeModifiedAttributes.multiply(*args, **kwargs)
        
    def boostChargeAttr(self, *args, **kwargs):
        self.chargeModifiedAttributes.boost(*args, **kwargs)