#Item: Siege Warfare [Skill]
#Item: Siege Warfare Mindlink [Implant]
type = "gang"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("shieldCapacityBonus") * level)
