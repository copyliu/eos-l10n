#Used by:
#Ship: Enyo
#Ship: Harpy
#Ship: Ishkur
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("eliteBonusGunship1") * level)