#Used by:
#Ship: Golem
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                    "aoeVelocity", ship.getModifiedItemAttr("shipBonus2CB") * level)
