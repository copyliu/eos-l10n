#Variations of item: Moa (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.ship.boostItemAttr("shieldEmDamageResonance", ship.getModifiedItemAttr("shipBonusCC2") * level)