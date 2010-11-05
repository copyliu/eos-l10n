#Used by:
#Variations of ship: Maller (3 of 3)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.ship.boostItemAttr("armorThermalDamageResonance", ship.getModifiedItemAttr("shipBonusAC2") * level)
