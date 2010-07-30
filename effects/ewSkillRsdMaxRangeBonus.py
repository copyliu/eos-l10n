#Used by:
#Modules named like: Particle Dispersion Projector (6 of 6)
#Skill: Long Distance Jamming
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                  "maxRange", module.getModifiedItemAttr("rangeSkillBonus"),
                                  stackingPenalties = "skill" not in context)
