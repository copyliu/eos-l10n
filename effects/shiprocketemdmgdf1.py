# Used by:
# Ship: Heretic
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Destroyers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Rockets"),
                                    "emDamage", ship.getModifiedItemAttr("shipBonusDF1") * level)
