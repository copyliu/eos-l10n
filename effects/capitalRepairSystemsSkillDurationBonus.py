#Used by:
#Implants named like: Hardwiring Inherent Implants 'Gentry' ZEX (3 of 6)
#Skill: Capital Repair Systems
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Repair Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
