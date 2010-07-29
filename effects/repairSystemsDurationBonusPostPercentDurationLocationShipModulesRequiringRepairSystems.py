#Items with name like: Nanobot Accelerator (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Armor Implants (3 of 3)
#Item: Numon Family Heirloom [Implant]
#Item: Repair Systems [Skill]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "duration", container.getModifiedItemAttr("durationSkillBonus"),
                                  stackingPenalties = "skill" not in context and "implant" not in context)
