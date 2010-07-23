#Variations of item: Large Warhead Flare Catalyst I (2 of 2) [Module]
#Variations of item: Medium Warhead Flare Catalyst I (2 of 2) [Module]
#Variations of item: Small Warhead Flare Catalyst I (2 of 2) [Module]
#Item: Hardwiring - Zainou 'Deadeye' ZMS10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMS100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMS1000 [Implant]
#Item: Target Navigation Prediction [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeVelocity", container.getModifiedItemAttr("aoeVelocityBonus") * level,
                                    stackingPenalties = context != "skill" and context != "implant")