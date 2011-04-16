#Used by:
#Implants from group: Booster (9 of 35)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", booster.getModifiedItemAttr("boosterArmorRepairAmountPenalty"))