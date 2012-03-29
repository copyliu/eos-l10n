# Used by:
# Ship: Cerberus
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Assault Missiles"),
                                    "explosionDelay", ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level)
