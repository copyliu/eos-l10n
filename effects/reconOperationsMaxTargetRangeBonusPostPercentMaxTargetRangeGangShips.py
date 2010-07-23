#Item: Information Warfare [Skill]
#Item: Information Warfare Mindlink [Implant]
type = "gang"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus") * level)