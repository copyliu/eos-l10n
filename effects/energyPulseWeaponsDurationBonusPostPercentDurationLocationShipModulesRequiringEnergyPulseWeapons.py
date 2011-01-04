#Used by:
#Implants named like: Hardwiring Inherent Implants 'Squire' EP (3 of 3)
#Skill: Energy Pulse Weapons
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Energy Pulse Weapons"),
                                  "duration", container.getModifiedItemAttr("durationBonus") * level)