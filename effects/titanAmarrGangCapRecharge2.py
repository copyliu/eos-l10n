#Used by:
#Ship: Avatar
type = "gang"
gangBoost = "rechargeRate"
gangBonus = "titanAmarrBonus2"
gangSkill = "Amarr Titan"
def handler(fit, ship, context):
    fit.ship.boostItemAttr(gangBoost, ship.getModifiedItemAttr(gangBonus))
