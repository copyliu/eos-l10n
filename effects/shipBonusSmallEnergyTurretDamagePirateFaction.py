#Item: Cruor [Ship]
#Item: Succubus [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusPirateFaction"))