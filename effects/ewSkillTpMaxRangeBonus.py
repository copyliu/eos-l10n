#Used by:
#Modules named like: Particle Dispersion Projector (6 of 6)
#Skill: Long Distance Jamming
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Target Painter",
                                  "maxRange", container.getModifiedItemAttr("rangeSkillBonus") * level)
