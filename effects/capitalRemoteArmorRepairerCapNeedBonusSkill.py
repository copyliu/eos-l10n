#Item: Capital Remote Armor Repair Systems [Skill]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX20 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX200 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX2000 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Remote Armor Repair Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
