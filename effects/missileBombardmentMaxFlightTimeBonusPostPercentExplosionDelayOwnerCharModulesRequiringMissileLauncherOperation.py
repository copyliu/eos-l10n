#Variations of item: Large Rocket Fuel Cache Partition I (2 of 2) [Module]
#Variations of item: Medium Rocket Fuel Cache Partition I (2 of 2) [Module]
#Variations of item: Small Rocket Fuel Cache Partition I (2 of 2) [Module]
#Item: Hardwiring - Zainou 'Deadeye' ZMC10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMC100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMC1000 [Implant]
#Item: Missile Bombardment [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                    "explosionDelay", container.getModifiedItemAttr("maxFlightTimeBonus") * level)