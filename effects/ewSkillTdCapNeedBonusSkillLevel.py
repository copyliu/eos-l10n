#Used by:
#Implants named like: Hardwiring Zainou 'Gypsy' KSB (6 of 6)
#Skill: Weapon Disruption
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Weapon Disruption"),
                                  "capacitorNeed", skill.getModifiedItemAttr("capNeedBonus") * skill.level)