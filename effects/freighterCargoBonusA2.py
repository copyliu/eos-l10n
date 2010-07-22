#Variations of item: Providence (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Freighter").level
    fit.ship.boostItemAttr("capacity", ship.getModifiedItemAttr("freighterBonusA2") * level)