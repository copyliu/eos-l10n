#Used by:
#Modules from group: Capacitor Booster (54 of 54)
type = "active"
def handler(fit, module, context):
    if module.charge == None: return
    #This is quite the effect compared to most others.
    #So an explanation is probably at hand.
    
    #Step 1: We fetch all the attributes we'll need
    capAmount = module.getModifiedChargeAttr("capacitorBonus")
    rate = module.getModifiedItemAttr("duration") / 1000.0
    chargeSize = module.getModifiedChargeAttr("volume")
    boosterSize = module.getModifiedItemAttr("capacity")
    
    #Calculate the amount of boosts that we can do before running out of ammo
    numBoosts = int(boosterSize / chargeSize)
    
    #Calculate the cycleTime, this is amount of boosts * rate
    #We also add 10 second for the reload time
    cycleTime = numBoosts * rate + 10
    
    #Calculate the amount of cap we get per cycle.
    cycleAmount = capAmount * numBoosts
    
    #Add the boost per second to the fit
    fit.extraAttributes["capBoost"].increase(cycleAmount / cycleTime)
    fit.capBoost += cycleAmount / cycleTime