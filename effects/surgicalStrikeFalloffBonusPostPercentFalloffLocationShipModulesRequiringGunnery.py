#Item: Hardwiring - Zainou 'Deadeye' ZGC10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGC100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGC1000 [Implant]
#Item: Improved Sooth Sayer Booster [Implant]
#Item: Standard Sooth Sayer Booster [Implant]
#Item: Strong Sooth Sayer Booster [Implant]
#Item: Synth Sooth Sayer Booster [Implant]
#Item: Trajectory Analysis [Skill]
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "falloff", container.getModifiedItemAttr("falloffBonus") * level)