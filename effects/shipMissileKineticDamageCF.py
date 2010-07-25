#Variations of item: Condor (2 of 3) [Ship]
#Variations of item: Heron (2 of 2) [Ship]
#Item: Caldari Navy Hookbill [Ship]
#Item: Hawk [Ship]
#Item: Kestrel [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "kineticDamage", ship.getModifiedItemAttr("shipBonusCF") * level)