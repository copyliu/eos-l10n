#Used by:
#Ship: Ragnarok
type = "gang"
gangBoost = "signatureRadius"
gangBonus = "titanMinmatarBonus2"
gangSkill = "Minmatar Titan"
def handler(fit, ship, context):
    level = fit.character.getSkill(gangSkill).level
    fit.ship.boostItemAttr(gangBoost, ship.getModifiedItemAttr(gangBonus) * level)
