#Used by:
#Modules from group: Hybrid Weapon (197 of 197)
#Modules from group: Projectile Weapon (141 of 141)
type = 'active'
def handler(fit, module, context):
    # Set reload time to 10 seconds
    module.reloadTime = 10000
    if module.charge is not None:
        # Set number of cycles before reload is needed
        chargeRate = module.getModifiedItemAttr("chargeRate")
        numCharges = module.numCharges
        module.numShots = float(numCharges) / chargeRate
    else:
        module.numShots = 0
