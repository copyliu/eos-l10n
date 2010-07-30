#Used by:
#Ship: Golem
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Cruise Missile"),
                                    "aoeVelocity", ship.getModifiedItemAttr("shipBonus2CB") * level)