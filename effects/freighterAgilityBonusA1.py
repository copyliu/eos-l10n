#Item: Ark [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Freighter").level
    fit.ship.boostItemAttr("agility", ship.getModifiedItemAttr("freighterBonusA1") * level)