#Items from group: Effect Beacon (6 of 38) [Celestial]
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                     "damageMultiplier", module.getModifiedItemAttr("smallWeaponDamageMultiplier"))