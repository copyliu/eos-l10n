#Item: Hardwiring - Zainou 'Gnome' KZA1000 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KZA2000 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KZA500 [Implant]
#Item: Weapon Upgrades [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus") * level)