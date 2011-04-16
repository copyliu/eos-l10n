#Used by:
#Ship: Flycatcher
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Destroyers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles"),
                                    "aoeVelocity", ship.getModifiedItemAttr("shipBonusDF2") * level)
