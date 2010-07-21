#Item: Viator [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Transport Ships").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Repair Unit",
                                  "duration", ship.getModifiedItemAttr("eliteBonusIndustrial2") * level)