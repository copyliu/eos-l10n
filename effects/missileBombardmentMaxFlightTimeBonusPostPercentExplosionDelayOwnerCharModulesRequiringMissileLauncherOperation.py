#Items with name like: Rocket Fuel Cache Partition (6 of 6)
#Item: Hardwiring - Zainou 'Deadeye' ZMC10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMC100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMC1000 [Implant]
#Item: Missile Bombardment [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "explosionDelay", container.getModifiedItemAttr("maxFlightTimeBonus") * level)
