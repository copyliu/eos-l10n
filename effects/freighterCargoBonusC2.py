#Variations of item: Charon (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Freighter").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("freighterBonusC2") * level)