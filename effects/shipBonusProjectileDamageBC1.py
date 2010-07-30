#Used by:
#Ship: Hurricane
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                    "damageMultiplier", ship.getModifiedItemAttr("shipBonusBC1") * level)