# Used by:
# Ship: Hawk
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation"),
                                  "shieldBonus", ship.getModifiedItemAttr("eliteBonusGunship2") * level)
