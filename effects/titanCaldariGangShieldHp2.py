#Used by:
#Ship: Leviathan
type = "gang"
gangBoost = "shieldCapacity"
gangBonus = "shipBonusCT2"
gangSkill = "Caldari Titan"
def handler(fit, ship, context):
    fit.ship.boostItemAttr(gangBoost, ship.getModifiedItemAttr(gangBonus))
