#Used by:
#Ship: Adrestia
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                    "falloff", ship.getModifiedItemAttr("shipBonusATC2"))