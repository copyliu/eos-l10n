#Used by:
#Items from market group: Ships > Carriers > Amarr (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    for armorType in ("Explosive" ,"Kinetic", "Em", "Thermal"):
        fit.ship.boostItemAttr("armor%sDamageResonance" % armorType, ship.getModifiedItemAttr("carrierAmarrBonus2") * level)