# Used by:
# Modules named like: Core Defence Capacitor Safeguard (6 of 6)
# Skill: Shield Compensation
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "capacitorNeed", container.getModifiedItemAttr("shieldBoostCapacitorBonus") * level)
