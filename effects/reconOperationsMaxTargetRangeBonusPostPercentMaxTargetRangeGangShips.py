#Item: Information Warfare [Skill]
#Item: Information Warfare Mindlink [Implant]
type = "gang"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus") * level)
