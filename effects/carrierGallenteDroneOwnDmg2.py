#Used by:
#Ship: Nyx
#Ship: Thanatos
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Carrier").level
    fit.drones.filteredItemBoost(lambda dron: dron.requiresSkill("Fighters"),
                                 "damageMultiplier", ship.getModifiedItemAttr("carrierGallenteBonus2") * level)
    