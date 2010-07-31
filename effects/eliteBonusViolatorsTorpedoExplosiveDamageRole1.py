#Used by:
#Ship: Golem
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Torpedoes"),
                                  "explosiveDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))