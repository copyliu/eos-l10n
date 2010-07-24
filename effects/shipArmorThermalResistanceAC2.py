#Variations of item: Maller (3 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.ship.boostItemAttr("armorThermalDamageResonance", ship.getModifiedItemAttr("shipBonusAC2") * level)