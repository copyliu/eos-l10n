#Used by:
#Ship: Golem
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Cruise Missiles"),
                                  "thermalDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))