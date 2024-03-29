# Used by:
# Ship: Drake
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles") or mod.charge.requiresSkill("Assault Missiles"),
                                    "kineticDamage", ship.getModifiedItemAttr("shipBonusBC1") * level)
