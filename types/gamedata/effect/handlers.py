def increase(module, attribute, increase):
    pass
    

def multiply(module, attrName, multiplier, bonusAttrCont = None, useStackingPenalty = False, extraMult = None, extraMultCont = None, addContAsSource = True):
    pass
        
def boost(module, attrName, bonus, bonusAttrCont = None, useStackingPenalty = False, extraMult = None, extraMultCont = None, addContAsSource = True):
    pass
                
def boostModListByReq(modList, attrName, bonus, moduleCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass

def boostAmmoListByReq(modList, attrName, bonus, ammoCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
            
def boostDroneListByReq(droneList, attrName, bonus, droneCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
            
def boostDroneListAmmoByReq(droneList, attrName, bonus, droneCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
            
def boostDroneListAmmoBySkillReq(droneList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
                
def boostBoosterListByReq(boosterList, attrName, bonus, boosterCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
            
def boostImplantListByReq(implantList, attrName, bonus, implantCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
            
def boostDroneListBySkillReq(droneList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass

def boostModListBySkillReq(modList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
                
def boostAmmoListBySkillReq(modList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    pass
