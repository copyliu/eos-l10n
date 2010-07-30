#Item: Cerberus [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Heavy Assault Missiles"),
                                    "explosionDelay", ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level)