#Used by:
#Items from market group: Ships > Carriers > Caldari (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Carrier").level
    for resType in ("Explosive", "Kinetic", "Em", "Thermal"):
        fit.ship.boostItemAttr("shield%sDamageResonance", ship.getModifiedAttribute("carrierCaldariBonus2") * level)    