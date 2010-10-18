#Used by:
#Skill: Armored Warfare
type = "gang", "passive"
def handler(fit, skill, context):
    if "gang" in context:
        fit.ship.boostItemAttr("armorHP", skill.getModifiedItemAttr("armorHpBonus") * skill.level)
    else:
        skill.commandBonus = skill.getModifiedItemAttr("armorHpBonus") * skill.level
