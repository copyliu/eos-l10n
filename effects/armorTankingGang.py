#Used by:
#Skill: Armored Warfare
type = "gang"
gangBonus = "armorHpBonus"
gangBoosts = "armorHP"
def handler(fit, skill, context):
    fit.ship.boostItemAttr("armorHP", skill.getModifiedItemAttr("armorHpBonus") * skill.level)
