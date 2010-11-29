#Used by:
#Implants named like: Hardwiring Zainou 'Sharpshooter' ZMX (3 of 3)
#Skill: Citadel Torpedoes
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Citadel Torpedoes"),
                                    "emDamage", container.getModifiedItemAttr("damageMultiplierBonus") * level)
