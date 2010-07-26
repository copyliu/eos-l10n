#Item: Skirmish Warfare [Skill]
#Item: Skirmish Warfare Mindlink [Implant]
type = "gang"
def handler(fit, container, context):
    level = container.level if context == "gangskill" else 1
    fit.ship.boostItemAttr("agility", container.getModifiedItemAttr("agilityBonus") * level)