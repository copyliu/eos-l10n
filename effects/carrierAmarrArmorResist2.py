#Used by:
#Ship: Aeon
#Ship: Archon
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    for armorType in ("Explosive" ,"Kinetic", "Em", "Thermal"):
        fit.ship.boostItemAttr("armor%sDamageResonance" % armorType, ship.getModifiedItemAttr("carrierAmarrBonus2") * level)