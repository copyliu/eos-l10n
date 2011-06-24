# Used by:
# Variations of ship: Caracal (3 of 3)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusCC2") * level)
