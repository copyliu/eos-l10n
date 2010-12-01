#Used by:
#Ship: Viator
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Transport Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "duration", ship.getModifiedItemAttr("eliteBonusIndustrial2") * level)
