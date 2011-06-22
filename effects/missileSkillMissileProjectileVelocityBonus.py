# Used by:
# Implants named like: Hardwiring Zainou 'Deadeye' ZML (6 of 6)
# Modules named like: Hydraulic Bay Thrusters (6 of 6)
# Skill: Missile Projection
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "maxVelocity", container.getModifiedItemAttr("speedFactor") * level,
                                    stackingPenalties = "skill" not in context and "implant" not in context)
