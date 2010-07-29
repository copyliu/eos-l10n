#Items with name like: Warhead Flare Catalyst (6 of 6)
#Item: Hardwiring - Zainou 'Deadeye' ZMS10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMS100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMS1000 [Implant]
#Item: Target Navigation Prediction [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeVelocity", container.getModifiedItemAttr("aoeVelocityBonus") * level,
                                    stackingPenalties = "skill" not in context and "implant" not in context)
