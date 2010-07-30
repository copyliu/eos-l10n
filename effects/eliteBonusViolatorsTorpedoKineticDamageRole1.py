#Used by:
#Ship: Golem
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Torpedoes"),
                                  "kineticDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))