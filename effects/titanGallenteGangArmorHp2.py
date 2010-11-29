#Used by:
#Ship: Erebus
type = "gang"
gangBoost = "armorHP"
gangBonus = "titanGallenteBonus2"
gangSkill = "Gallente Titan"
def handler(fit, ship, context):
    level = fit.character.getSkill(gangSkill).level
    fit.ship.boostItemAttr(gangBoost, ship.getModifiedItemAttr(gangBonus) * level)
