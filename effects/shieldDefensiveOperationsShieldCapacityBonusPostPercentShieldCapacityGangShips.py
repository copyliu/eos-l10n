#Item: Siege Warfare [Skill]
#Item: Siege Warfare Mindlink [Implant]
type = "gang"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("shieldCapacityBonus") * level)