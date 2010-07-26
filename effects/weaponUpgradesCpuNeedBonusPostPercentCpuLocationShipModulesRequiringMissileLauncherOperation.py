#Item: Hardwiring - Zainou 'Gnome' KTA10 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KTA100 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KTA1000 [Implant]
#Item: Weapon Upgrades [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus") * level)