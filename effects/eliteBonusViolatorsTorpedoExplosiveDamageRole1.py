#Used by:
#Ship: Golem
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                    "explosiveDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))
