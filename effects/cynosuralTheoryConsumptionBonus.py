#Items from group: Force Recon Ship (4 of 4) [Ship]
#Item: Cynosural Field Theory [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Cynosural Field Theory"),
                                  "consumptionQuantity", container.getModifiedItemAttr("consumptionQuantityBonusPercentage") * level)
