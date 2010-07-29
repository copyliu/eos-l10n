#Item: Hardwiring - Zainou 'Deadeye' ZGA10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGA100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGA1000 [Implant]
#Item: Improved Frentix Booster [Implant]
#Item: Sharpshooter [Skill]
#Item: Standard Frentix Booster [Implant]
#Item: Strong Frentix Booster [Implant]
#Item: Synth Frentix Booster [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "maxRange", container.getModifiedItemAttr("rangeSkillBonus") * level)
