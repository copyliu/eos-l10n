#Used by:
#Ship: Nighthawk
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Command Ships").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "kineticDamage", ship.getModifiedItemAttr("eliteBonusCommandShips1") * level)
