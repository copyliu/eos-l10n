#Variations of item: Large Core Defence Capacitor Safeguard I (2 of 2) [Module]
#Variations of item: Medium Core Defence Capacitor Safeguard I (2 of 2) [Module]
#Variations of item: Small Core Defence Capacitor Safeguard I (2 of 2) [Module]
#Item: Shield Compensation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "capacitorNeed", container.getModifiedItemAttr("shieldBoostCapacitorBonus") * level,
                                  stackingPenalties = "skill" not in context)
