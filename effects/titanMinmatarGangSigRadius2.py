#Used by:
#Ship: Ragnarok
type = "gang"
gangSkill = "Minmatar Titan"
gangBonus = "titanMinmatarBonus2"
gangBoost = "signatureRadius"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Titan").level
    fit.ship.boostItemAttr("signatureRadius", ship.getModifiedItemAttr("titanMinmatarBonus2") * level)
