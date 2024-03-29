# Used by:
# Implants named like: Zainou 'Deadeye' Target Navigation Prediction TN (6 of 6)
# Modules named like: Warhead Flare Catalyst (6 of 6)
# Skill: Target Navigation Prediction
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "aoeVelocity", container.getModifiedItemAttr("aoeVelocityBonus") * level,
                                    stackingPenalties = "skill" not in context and "implant" not in context)
