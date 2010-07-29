#Item: Gunnery [Skill]
#Item: Hardwiring - Inherent Implants 'Lancer' G0-Delta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Delta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Delta [Implant]
#Item: Pashan's Turret Customization Mindlink [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "speed", container.getModifiedItemAttr("turretSpeeBonus") * level)
