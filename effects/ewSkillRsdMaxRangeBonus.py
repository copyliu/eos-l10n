#Variations of item: Large Particle Dispersion Projector I (2 of 2) [Module]
#Variations of item: Medium Particle Dispersion Projector I (2 of 2) [Module]
#Variations of item: Small Particle Dispersion Projector I (2 of 2) [Module]
#Item: Long Distance Jamming [Skill]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                  "maxRange", module.getModifiedItemAttr("rangeSkillBonus"),
                                  stackingPenalties = context != "skill")