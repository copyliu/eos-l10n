#Used by:
#Ship: Utu
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                    "trackingSpeed", ship.getModifiedItemAttr("shipBonusATF2") * level)