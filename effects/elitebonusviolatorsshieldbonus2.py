# Used by:
# Ship: Golem
# Ship: Vargur
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Marauders").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", ship.getModifiedItemAttr("eliteBonusViolators2") * level)
