from model.attribute import basicAttribute

def increase(module, attrName, increase, bonusAttrCont = None, useStackingPenalty = False, extraMult = None, extraMultCont = None, position = "pre", addContAsSource = True):
    if module.ID == 0: return
    if useStackingPenalty == True:
        raise ValueError("Can't apply stacking penalties to a plain increase")
    
    if isinstance(increase, str):
        increase = bonusAttrCont.getModifiedAttribute(increase)
        if increase == None:
            return
        
    if isinstance(attrName, tuple):
        for name in attrName:
            increase(module, name, increase, bonusAttrCont, useStackingPenalty, extraMult, extraMultCont)
        
        return
    
    if attrName in module.attributes: currAttr = module.attributes[attrName]
    else:
        currAttr = basicAttribute(module, attrName, None, 0)
        module.attributes[attrName] = currAttr
        
    if isinstance(extraMult, str):
        extraMultCont = extraMultCont or bonusAttrCont
        extraMult = extraMultCont.getModifiedAttribute(extraMult)
        
    if extraMult != None: increase = increase * extraMult  
    if addContAsSource and bonusAttrCont: currAttr.addSource(bonusAttrCont)
    currAttr.increase(increase, position = position)

def multiply(module, attrName, multiplier, bonusAttrCont = None, useStackingPenalty = False, extraMult = None, extraMultCont = None, addContAsSource = True):
    if module.ID == 0: return
    if isinstance(multiplier, str):
        multiplier = bonusAttrCont.getModifiedAttribute(multiplier)
        if multiplier == None:
            return
        
    if isinstance(attrName, tuple):
        for name in attrName:
            multiply(module, name, multiplier, bonusAttrCont, useStackingPenalty, extraMult, extraMultCont)
        
        return
    
    if attrName in module.attributes:
        currAttr = module.attributes[attrName]
        if isinstance(extraMult, str):
            extraMultCont = extraMultCont or bonusAttrCont
            extraMult = extraMultCont.getModifiedAttribute(extraMult)
        if extraMult != None: multiplier = multiplier * extraMult
        currAttr.multiply(multiplier, useStackingPenalty)
        if addContAsSource and bonusAttrCont: currAttr.addSource(bonusAttrCont)
        
def boost(module, attrName, bonus, bonusAttrCont = None, useStackingPenalty = False, extraMult = None, extraMultCont = None, addContAsSource = True):
    '''
    Boost the passed module in the passed attribute by the passed bonus divided by 100
    @param module: The module to boost
    @param attrName: What attribute from the module to boost
    @param bonus: By how much to boost it.
    @param bonusAttrCont: the item to get the bonus attribute from if bonus was a string
    @param useStackingPenalty: Wether to apply with or without stacking penalties
    '''
    if module.ID == 0: return
    if isinstance(bonus, str):
        bonus = bonusAttrCont.getModifiedAttribute(bonus)
        if bonus == None:
            return
        
    if isinstance(attrName, tuple):
        for name in attrName:
            boost(module, name, bonus, bonusAttrCont, useStackingPenalty, extraMult, extraMultCont)
        
        return    
    
    if isinstance(extraMult, str):
        extraMult = extraMultCont.getModifiedAttribute(extraMult)
        
    if extraMult != None: bonus = bonus * extraMult
    if attrName in module.attributes:
        currAttr = module.attributes[attrName]
        currAttr.multiply(1 + bonus / 100.0, useStackingPenalty)
        if addContAsSource and bonusAttrCont: currAttr.addSource(bonusAttrCont)
                
def boostModListByReq(modList, attrName, bonus, moduleCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for module in modList:
        item = module.getItem()
        if item.ID != 0 and moduleCondition(item):
            helper(item, attrName, bonus, bonusAttrCont, **kwargs)

def boostAmmoListByReq(modList, attrName, bonus, ammoCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for module in modList:
        ammo = module.getAmmo()
        if ammo != None and ammoCondition(ammo):
            helper(ammo, attrName, bonus, bonusAttrCont, **kwargs)
            
def boostDroneListByReq(droneList, attrName, bonus, droneCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for drone in droneList:
        item = drone.getItem()
        if droneCondition(item):
            helper(item, attrName, bonus, bonusAttrCont, **kwargs)
            
def boostDroneListAmmoByReq(droneList, attrName, bonus, droneCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for drone in droneList.iteritems():
        item = drone.getItem()
        ammo = drone.getAmmo()
        if ammo and droneCondition(item):
            helper(ammo, attrName, bonus, bonusAttrCont, **kwargs)
            
def boostDroneListAmmoBySkillReq(droneList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for drone in droneList:
        item = drone.getItem()
        ammo = drone.getAmmo()
        if ammo:
            for skill in item.requiredSkills:
                if skillCondition(skill):
                    helper(ammo, attrName, bonus, bonusAttrCont, **kwargs)
                    break
                
def boostBoosterListByReq(boosterList, attrName, bonus, boosterCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for booster, activeSideEffects in boosterList.itervalues():
        if boosterCondition(booster):
            helper(booster, attrName, bonus, bonusAttrCont, **kwargs)
            
def boostImplantListByReq(implantList, attrName, bonus, implantCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for implant in implantList.itervalues():
        if implantCondition(implant):
            helper(implant, attrName, bonus, bonusAttrCont, **kwargs)
            
def boostDroneListBySkillReq(droneList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for drone in droneList:
        item = drone.getItem()
        for skill in item.requiredSkills:
            if skillCondition(skill):
                helper(item, attrName, bonus, bonusAttrCont, **kwargs)
                break

def boostModListBySkillReq(modList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for module in modList:
        item = module.getItem()
        for skill in item.requiredSkills:
            if skillCondition(skill):
                helper(item, attrName, bonus, bonusAttrCont, **kwargs)
                break
                
def boostAmmoListBySkillReq(modList, attrName, bonus, skillCondition, bonusAttrCont = None, helper = boost, **kwargs):
    for module in modList:
        ammo = module.getAmmo()
        if ammo != None:
            for skill in ammo.requiredSkills:
                if skillCondition(skill):
                    helper(ammo, attrName, bonus, bonusAttrCont, **kwargs)
                    break
