#Variations of item: Obelisk (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Freighter").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("freighterBonusG2") * level)