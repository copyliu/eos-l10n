#Item: Fenrir [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Freighter").level
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("freighterBonusM1") * level)