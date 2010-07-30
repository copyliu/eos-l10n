#Used by:
#Ship: Ashimmu
#Ship: Phantasm
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusPirateFaction"))