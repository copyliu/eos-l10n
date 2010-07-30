#Items with name like: Missile Specialization (4 of 4)
#Item: Rocket Specialization [Skill]
#Item: Torpedo Specialization [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill(skill),
                                  "speed", skill.getModifiedItemAttr("rofBonus") * skill.level)