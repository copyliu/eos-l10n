#Variations of item: Large Hydraulic Bay Thrusters I (2 of 2) [Module]
#Variations of item: Medium Hydraulic Bay Thrusters I (2 of 2) [Module]
#Variations of item: Small Hydraulic Bay Thrusters I (2 of 2) [Module]
#Item: Hardwiring - Zainou 'Deadeye' ZML10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZML100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZML1000 [Implant]
#Item: Missile Projection [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "maxVelocity", container.getModifiedItemAttr("speedFactor") * level,
                                    stackingPenalties = "skill" not in context and "implant" not in context)
