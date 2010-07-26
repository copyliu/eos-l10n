#Items from group: Effect Beacon (6 of 38) [Celestial]
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Smart Bomb",
                                     "explosiveDamage", module.getModifiedItemAttr("smartbombDamageMultiplier"))