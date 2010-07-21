#Item: Golem [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Cruise Missiles"),
                                  "emDamage", ship.getModifiedItemAttr("eliteBonusViolatorsRole1"))