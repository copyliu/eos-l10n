#Item: Zealot [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "maxRange", ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level)