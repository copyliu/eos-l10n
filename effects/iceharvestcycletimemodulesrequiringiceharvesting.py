# Used by:
# Implants named like: Inherent Implants 'Yeti' Ice Harvesting IH (3 of 3)
# Ship: Mackinaw
# Skill: Ice Harvesting
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Ice Harvesting"),
                                  "duration", container.getModifiedItemAttr("iceHarvestCycleBonus") * level)
