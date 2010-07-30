#Item: Caldari Navy Hookbill [Ship]
#Item: Condor [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusCF2") * level)