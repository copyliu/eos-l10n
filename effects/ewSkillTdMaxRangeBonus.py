#Items with name like: Particle Dispersion Projector (6 of 6)
#Item: Long Distance Jamming [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Disruptor",
                                  "maxRange", container.getModifiedItemAttr("rangeSkillBonus") * level,
                                  stackingPenalties = "skill" not in context and "implant" not in context)
