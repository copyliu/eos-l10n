#Used by:
#Ship: Erebus
type = "gang"
gangSkill = "Gallente Titan"
gangBonus = "titanGallenteBonus2"
gangBoost = "armorHP"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Titan").level
    fit.ship.boostItemAttr("armorHP", fit.ship.getModifiedItemAttr("titanGallenteBonus2") * level)
