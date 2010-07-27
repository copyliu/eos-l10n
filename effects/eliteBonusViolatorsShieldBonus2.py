#Item: Golem [Ship]
#Item: Vargur [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Marauders").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", ship.getModifiedItemAttr("eliteBonusViolators2") * level)