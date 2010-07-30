#Used by:
#Ship: Buzzard
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "speed", ship.getModifiedItemAttr("shipBonusCF") * level)