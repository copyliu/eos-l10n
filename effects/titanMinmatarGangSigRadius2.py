#Used by:
#Ship: Ragnarok
type = "gang"
gangBoost = "signatureRadius"
gangBonus = "titanMinmatarBonus2"
gangSkill = "Minmatar Titan"
def handler(fit, ship, context):
    fit.ship.boostItemAttr(gangBoost, ship.getModifiedItemAttr(gangBonus))
