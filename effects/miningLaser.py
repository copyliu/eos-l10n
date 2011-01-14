#Used by:
#Modules from group: Frequency Mining Laser (3 of 3)
#Modules from group: Mining Laser (17 of 17)
#Modules from group: Strip Miner (5 of 5)
type = 'active'
def handler(fit, module, context):
    # Set reload time to 1 second
    module.reloadTime = 1000
    if module.charge is not None:
        if module.getModifiedChargeAttr("crystalsGetDamaged") == 1:
            # For depletable crystals, calculate average amount of shots before it's destroyed
            hp = module.getModifiedChargeAttr("hp")
            chance = module.getModifiedChargeAttr("crystalVolatilityChance")
            damage = module.getModifiedChargeAttr("crystalVolatilityDamage")
            module.numShots = float(hp) / (damage * chance)
        else:
            # Set 0 (infinite) for permanent crystals like t1
            module.numShots = 0
    else:
        module.numShots = 0
