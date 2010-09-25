#Used by:
#Skill: Tactical Shield Manipulation
type = "passive"
def handler(fit, skill, context):
    bonus = (1 - fit.ship.getModifiedItemAttr("shieldUniformity")) /  5
    fit.ship.increaseItemAttr("shieldUniformity", bonus * skill.level)
