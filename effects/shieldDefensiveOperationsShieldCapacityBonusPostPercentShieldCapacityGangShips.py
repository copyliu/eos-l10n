#Used by:
#Implant: Siege Warfare Mindlink
#Skill: Siege Warfare
type = "gang", "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    if "gang" in context:
        fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("shieldCapacityBonus") * level)
    else:
        container.commandBonus = container.getModifiedItemAttr("shieldCapacityBonus") * level
