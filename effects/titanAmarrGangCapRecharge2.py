#Used by:
#Ship: Avatar
type = "gang"
gangSkill = "Amarr Titan"
gangBonus = "titanAmarrBonus2"
gangBoost = "rechargeRate"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Titan").level
    fit.ship.boostItemAttr("rechargeRate", ship.getModifiedItemAttr("titanAmarrBonus2") * level)
