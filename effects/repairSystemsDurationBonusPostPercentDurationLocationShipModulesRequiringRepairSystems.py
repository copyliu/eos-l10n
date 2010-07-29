#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Armor Implants (3 of 3)
#Variations of item: Large Nanobot Accelerator I (2 of 2) [Module]
#Variations of item: Medium Nanobot Accelerator I (2 of 2) [Module]
#Variations of item: Small Nanobot Accelerator I (2 of 2) [Module]
#Item: Numon Family Heirloom [Implant]
#Item: Repair Systems [Skill]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "duration", container.getModifiedItemAttr("durationSkillBonus"),
                                  stackingPenalties = "skill" not in context and "implant" not in context)
