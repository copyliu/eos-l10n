#Items with name like: Red Giant Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Smart Bomb",
                                     "explosiveDamage", module.getModifiedItemAttr("smartbombDamageMultiplier"))