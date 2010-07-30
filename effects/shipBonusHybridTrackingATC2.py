#Item: Adrestia [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                    "trackingSpeed", ship.getModifiedItemAttr("shipBonusATC2"))