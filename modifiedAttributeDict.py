import math

class ItemAttrShortcut(object):
    def getModifiedItemAttr(self, key):
        if key in self.itemModifiedAttributes:
            return self.itemModifiedAttributes[key]
        else:
            return None
    
class ChargeAttrShortcut(object):
    def getModifiedChargeAttr(self, key):
        if key in self.chargeModifiedAttributes:
            return self.chargeModifiedAttributes[key]
        else:
            return None
    
class ModifiedAttributeDict(object):
    class CalculationPlaceholder():
        pass
    
    def __init__(self):
        self.__modified = {}
        self.__original = None
        self.__preIncreases = {}
        self.__postIncreases = {}
        self.__multipliers = {}
        self.__penalizedMultipliers = {}
        
    def clear(self):
        self.__modified.clear()
        self.__preIncreases.clear()
        self.__postIncreases.clear()
        self.__multipliers.clear()
        self.__penalizedMultipliers.clear()
    
    @property
    def original(self):
        return self.__original
    
    @original.setter
    def original(self, val):
        self.__original = val
        self.__modified.clear()
        
    def __getitem__(self, key):
        if key in self.__modified:
            if self.__modified[key] == self.CalculationPlaceholder:
                self.__modified[key] = self.__calculateValue(key)
            return self.__modified[key]
        else:
            return self.__original[key].value
    
    def __setitem__(self, key, val):
        self.__modified[key] = val
    
    def __iter__(self):
        all = dict(self.__original, **self.__modified)
        return (key for key in all)
    
    def __contains__(self, key):
        return (self.__original != None and key in self.__original) or key in self.__modified
    
    def iterkeys(self):
        for key in self:
            yield key
    
    def itervalues(self):
        for key in self:
            yield self[key]
    
    def iteritems(self):
        for key in self:
            yield key, self[key]

    iter = __iter__            
    items = iteritems
    keys = iterkeys
    values = itervalues
    
    def __calculateValue(self, key):
        highIsGood = self.__original[key].highIsGood if self.__original.has_key(key) else True
        preIncrease = self.__preIncreases[key] if self.__preIncreases.has_key(key) else 0
        postIncrease = self.__postIncreases[key] if self.__postIncreases.has_key(key) else 0
        multiplier = self.__multipliers[key] if self.__multipliers.has_key(key) else 1
        penalizedMultiplierGroups = self.__penalizedMultipliers[key] if self.__penalizedMultipliers.has_key(key) else {}
        val = self.__original[key].value if self.__original.has_key(key) else 0
        
        if not isinstance(val, (int, long, float)):
            return val
        
        #We'll do stuff in the following order:
        #Preincreass, then multipliers
        #then stacking penalized multipliers, then postIncreases
        val += preIncrease
        val *= multiplier
        
        if len(penalizedMultiplierGroups) > 0:
            #Each group is penalized independantly
            #Things in different groups will not be stack penaltied between eachother
            for penalizedMultipliers in penalizedMultiplierGroups.itervalues():
                #A quick explanation of how this works:
                #1: Bonusses and penalties are penalized seperatly, so we'll have to filter each of them
                l1 = filter(lambda val: val > 1, penalizedMultipliers)
                l2 = filter(lambda val: val < 1, penalizedMultipliers)
                #2: The most significant bonusses take the smallest penalty,
                #This means we'll have to sort 
                abssort = lambda val: -abs(val -1)
                l1.sort(key=abssort)
                l2.sort(key=abssort)
                #3: The first module doesn't get penaltied at all
                #Any modul after the first takes penalties according to:
                #1 + (multplier - 1) * math.exp(- math.pow(i, 2) / 7.1289)
                for l in (l1, l2):
                    for i in xrange(len(l)):
                        bonus = l[i]
                        val *= 1 + (bonus - 1) * math.exp(- math.pow(i, 2) / 7.1289)
        
        val += postIncrease
        return val
        
        
    def increase(self, attributeName, increase, position = "pre"):
        if position == "pre": tbl = self.__preIncreases
        elif position == "post": tbl = self.__postIncreases
        else: raise ValueError("position should be either pre or post")
        if not tbl.has_key(attributeName): tbl[attributeName] = 0
        tbl[attributeName] += increase
        self.__modified[attributeName] = self.CalculationPlaceholder
        
    def multiply(self, attributeName, multiplier, stackingPenalties = False, penaltyGroup = "default"):
        if stackingPenalties:
            if not self.__penalizedMultipliers.has_key(attributeName):
                self.__penalizedMultipliers[attributeName] = {}
            if not self.__penalizedMultipliers[attributeName].has_key(penaltyGroup):
                self.__penalizedMultipliers[attributeName][penaltyGroup] = []
            
            tbl = self.__penalizedMultipliers[attributeName][penaltyGroup]
            tbl.append(multiplier)
        else:
            if not self.__multipliers.has_key(attributeName):
                self.__multipliers[attributeName] = 1
            self.__multipliers[attributeName] *= multiplier
            
        self.__modified[attributeName] = self.CalculationPlaceholder
        
    def boost(self, attributeName, boostFactor, *args, **kwargs):
        self.multiply(attributeName, 1 + boostFactor / 100.0, *args, **kwargs)