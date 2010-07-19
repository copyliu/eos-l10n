#Item: Capital Repair Systems [Skill]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX10 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX100 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX1000 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.skill if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Repair Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)