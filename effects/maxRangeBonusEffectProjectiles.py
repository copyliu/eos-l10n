#Used by:
#Modules named like: Projectile Locus Coordinator (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "maxRange", module.getModifiedItemAttr("maxRangeBonus"),
                                  stackingPenalties = True)