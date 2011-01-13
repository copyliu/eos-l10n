#Used by:
#Drones from group: Combat Drone (73 of 73)
#Drones from group: Fighter Drone (4 of 4)
#Modules from group: Energy Weapon (181 of 181)
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
