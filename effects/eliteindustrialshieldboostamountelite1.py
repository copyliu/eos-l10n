# Used by:
# Ships from group: Transport Ship (4 of 8)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Transport Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation"),
                                  "shieldBonus", ship.getModifiedItemAttr("eliteBonusIndustrial1") * level)
