#Item: Citadel Torpedoes [Skill]
#Item: Hardwiring - Zainou 'Sharpshooter' ZMX10 [Implant]
#Item: Hardwiring - Zainou 'Sharpshooter' ZMX100 [Implant]
#Item: Hardwiring - Zainou 'Sharpshooter' ZMX1000 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Citadel Torpedoes"),
                                    "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus") * level)
