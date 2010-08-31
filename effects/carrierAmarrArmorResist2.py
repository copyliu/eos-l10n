#Used by:
#Ship: Aeon
#Ship: Archon
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier").level
    for resType in ("Explosive", "Kinetic", "Em", "Thermal"):
        fit.ship.boostItemAttr("armor" + resType + "DamageResonance",
                               ship.getModifiedItemAttr("carrierAmarrBonus2") * level)
