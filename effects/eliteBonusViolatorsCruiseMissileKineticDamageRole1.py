#Used by:
#Ship: Golem
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                    "kineticDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))
