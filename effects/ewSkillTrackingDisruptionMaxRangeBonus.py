#Items with name like: Tracking Diagnostic Subroutines (6 of 6)
#Item: Turret Destabilization [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    for attr in ("maxRangeBonus", "falloffBonus"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Disruptor",
                                      attr, container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level,
                                      stackingPenalties = "skill" not in context)
