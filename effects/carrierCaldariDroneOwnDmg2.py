#Used by:
#Ship: Revenant
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Carrier").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Fighters"),
                                 "damageMultiplier", ship.getModifiedItemAttr("carrierCaldariBonus2") * level)
