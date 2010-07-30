#Variations of item: Fenrir (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Freighter").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("freighterBonusM2") * level)