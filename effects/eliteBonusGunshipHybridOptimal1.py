#Items from market group: Ships > Assault Ships > Gallente (2 of 2)
#Item: Harpy [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("eliteBonusGunship1") * level)