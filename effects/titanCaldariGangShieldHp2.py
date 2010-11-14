#Used by:
#Ship: Leviathan
type = "gang"
gangSkill = "Caldari Titan"
gangBoost = "shieldCapacity"
gangBonus = "shipBonusCT2"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Titan").level
    fit.ship.boostItemAttr("shieldCapacity", ship.getModifiedItemAttr("shipBonusCT2") * level)
