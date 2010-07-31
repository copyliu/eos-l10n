#Used by:
#Modules named like: Nanobot Accelerator (6 of 6)
#Implant: Hardwiring - Inherent Implants 'Noble' ZET10
#Implant: Hardwiring - Inherent Implants 'Noble' ZET100
#Implant: Hardwiring - Inherent Implants 'Noble' ZET1000
#Implant: Numon Family Heirloom
#Skill: Repair Systems
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "duration", container.getModifiedItemAttr("durationSkillBonus"),
                                  stackingPenalties = "skill" not in context and "implant" not in context)
