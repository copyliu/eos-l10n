#Variations of item: Large Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Variations of item: Medium Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Variations of item: Small Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Item: Turret Destabilization [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tracking Disruptor",
                                  "trackingSpeedBonus", container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level)