#Used by:
#Implants named like: Hardwiring Inherent Implants 'Lancer' Delta (3 of 3)
#Implant: Pashan's Turret Customization Mindlink
#Skill: Gunnery
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "speed", container.getModifiedItemAttr("turretSpeeBonus") * level)
