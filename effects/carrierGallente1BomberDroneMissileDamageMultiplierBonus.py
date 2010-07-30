#Used by:
#Ship: Nyx
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Carrier").level
    for damageType in ("em", "kinetic", "thermal", "explosive"):
        fit.drones.filteredChargeBoost(lambda drone: drone.item.requiresSkill("Fighter Bombers"),
                                       "%sDamage" % damageType,
                                       ship.getModifiedItemAttr("carrierGallenteBonus2") * level)