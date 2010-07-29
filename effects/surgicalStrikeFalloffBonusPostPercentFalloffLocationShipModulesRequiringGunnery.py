#Items with name like: Sooth Sayer Booster (4 of 4)
#Item: Hardwiring - Zainou 'Deadeye' ZGC10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGC100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGC1000 [Implant]
#Item: Trajectory Analysis [Skill]
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "falloff", container.getModifiedItemAttr("falloffBonus") * level)
