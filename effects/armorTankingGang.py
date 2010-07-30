#Item: Armored Warfare [Skill]
type = "gang"
def handler(fit, skill, context):
    fit.ship.boostItemAttr("armorHP", skill.getModifiedItemAttr("armorHpBonus") * skill.level)