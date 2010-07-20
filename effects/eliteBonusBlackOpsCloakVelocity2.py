#Items from group: Black Ops (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    if not fit.cloaked: return
    level = fit.character.getSkill("Black Ops").level
    bonus = ship.getModifiedItemAttr("eliteBonusBlackOps2")
    multiplier = pow(bonus, level)
    fit.ship.multiplyItemAttr("maxVelocity", multiplier)