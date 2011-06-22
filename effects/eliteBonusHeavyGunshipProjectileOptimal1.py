# Used by:
# Ship: Muninn
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "maxRange", ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level)
