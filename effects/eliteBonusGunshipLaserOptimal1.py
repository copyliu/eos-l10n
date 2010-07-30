#Item: Retribution [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "maxRange", ship.getModifiedItemAttr("eliteBonusGunship1") * level)