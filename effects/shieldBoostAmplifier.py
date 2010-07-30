#Items from group: Capacitor Power Relay (25 of 25) [Module]
#Items from group: Shield Boost Amplifier (25 of 25) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation") or mod.item.requiresSkill("Capital Shield Operation"),
                                  "shieldBonus", module.getModifiedItemAttr("shieldBoostMultiplier"),
                                  stackingPenalties = module.item.group.name == "Shield Boost Amplifier")