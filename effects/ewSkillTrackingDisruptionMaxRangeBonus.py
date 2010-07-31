#Used by:
#Modules named like: Tracking Diagnostic Subroutines (6 of 6)
#Skill: Turret Destabilization
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    for attr in ("maxRangeBonus", "falloffBonus"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Disruptor",
                                      attr, container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level,
                                      stackingPenalties = "skill" not in context)
