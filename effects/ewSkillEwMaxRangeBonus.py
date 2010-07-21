#Variations of item: Large Particle Dispersion Projector I (2 of 2) [Module]
#Variations of item: Medium Particle Dispersion Projector I (2 of 2) [Module]
#Variations of item: Small Particle Dispersion Projector I (2 of 2) [Module]
#Item: Long Distance Jamming [Skill]
#Item: Low-grade Centurion Alpha [Implant]
#Item: Low-grade Centurion Beta [Implant]
#Item: Low-grade Centurion Delta [Implant]
#Item: Low-grade Centurion Epsilon [Implant]
#Item: Low-grade Centurion Gamma [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                  "maxRange", container.getModifiedItemAttr("rangeSkillBonus") * level,
                                  stackingPenalties = context != "skill" and context != "implant")