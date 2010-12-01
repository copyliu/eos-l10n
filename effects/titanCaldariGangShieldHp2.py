#Used by:
#Ship: Leviathan
type = "gang"
gangBoost = "shieldCapacity"
gangBonus = "shipBonusCT2"
gangSkill = "Caldari Titan"
def handler(fit, ship, context):
    level = fit.character.getSkill(gangSkill).level
    fit.ship.boostItemAttr(gangBoost, ship.getModifiedItemAttr(gangBonus) * level)
