#Used by:
#Ship: Avatar
type = "gang"
gangBoost = "rechargeRate"
gangBonus = "titanAmarrBonus2"
gangSkill = "Amarr Titan"
def handler(fit, ship, context):
    level = fit.character.getSkill(gangSkill).level
    fit.ship.boostItemAttr(gangBoost, ship.getModifiedItemAttr(gangBonus) * level)
