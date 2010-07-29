#Items with name like: Cataclysmic Variable Effect Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Armor Repair Projector",
                                  "armorDamageAmount", module.getModifiedItemAttr("armorDamageAmountMultiplier"))