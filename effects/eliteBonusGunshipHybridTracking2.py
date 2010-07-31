#Used by:
#Ship: Enyo
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Assault Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("eliteBonusGunship2") * level)