#Items with name like: Frentix Booster (4 of 4)
#Item: Hardwiring - Zainou 'Deadeye' ZGA10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGA100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGA1000 [Implant]
#Item: Sharpshooter [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "maxRange", container.getModifiedItemAttr("rangeSkillBonus") * level)
