#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Missile Implants (3 of 6)
#Item: Cerebral Accelerator [Implant]
#Item: Missile Launcher Operation [Skill]
#Item: Rapid Launch [Skill]
#Item: Whelan Machorin's Ballistic Smartlink [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                    "speed", container.getModifiedItemAttr("rofBonus") * level)