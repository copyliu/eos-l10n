#Item: Thrasher [Ship]
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "maxRange", container.getModifiedItemAttr("maxRangeBonus"))