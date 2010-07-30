#Items with name like: Particle Dispersion Projector (6 of 6)
#Item: Long Distance Jamming [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM Burst",
                                  "ecmBurstRange", container.getModifiedItemAttr("rangeSkillBonus") * level)
