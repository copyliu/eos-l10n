#Used by:
#Modules named like: Nanobot Accelerator (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Armor Implants (6 of 6)
#Implant: Numon Family Heirloom
#Skill: Repair Systems
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "duration", container.getModifiedItemAttr("durationSkillBonus") * level,
                                  stackingPenalties = "skill" not in context and "implant" not in context)
