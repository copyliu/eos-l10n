# Used by:
# Implants named like: Hardwiring Zainou 'Deadeye' ZMC (6 of 6)
# Modules named like: Rocket Fuel Cache Partition (6 of 6)
# Skill: Missile Bombardment
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "explosionDelay", container.getModifiedItemAttr("maxFlightTimeBonus") * level)
