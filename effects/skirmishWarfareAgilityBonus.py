#Used by:
#Implant: Skirmish Warfare Mindlink
#Skill: Skirmish Warfare
type = "gang", "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    if "gang" in context:
        fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("agilityBonus") * level)
    else:
        container.commandBonus = container.getModifiedItemAttr("agilityBonus") * level
