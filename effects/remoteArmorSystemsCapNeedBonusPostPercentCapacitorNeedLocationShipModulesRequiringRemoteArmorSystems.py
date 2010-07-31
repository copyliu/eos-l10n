#Used by:
#Modules named like: Remote Repair Augmentor (6 of 6)
#Implant: Hardwiring - Inherent Implants 'Noble' ZET20
#Implant: Hardwiring - Inherent Implants 'Noble' ZET200
#Implant: Hardwiring - Inherent Implants 'Noble' ZET2000
#Skill: Remote Armor Repair Systems
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Remote Armor Repair Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
