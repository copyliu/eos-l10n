#Used by:
#Implants named like: Hardwiring Inherent Implants 'Squire' EE (3 of 3)
#Modules named like: Egress Port Maximizer (6 of 6)
#Skill: Energy Emission Systems
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Energy Emission Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
