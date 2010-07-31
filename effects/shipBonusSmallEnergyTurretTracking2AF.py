#Used by:
#Ship: Succubus
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                    "trackingSpeed", ship.getModifiedItemAttr("shipBonus2AF") * level)