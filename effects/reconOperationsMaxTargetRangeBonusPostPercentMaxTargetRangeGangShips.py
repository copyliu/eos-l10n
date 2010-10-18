#Used by:
#Implant: Information Warfare Mindlink
#Skill: Information Warfare
type = "gang", "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    if "gang" in context:
        fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus") * level)
    else:
        container.commandBonus = container.getModifiedItemAttr("maxTargetRangeBonus") * level
