#Item: Golem [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Marauders").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Target Painter",
                                  "signatureRadiusBonus", ship.getModifiedItemAttr("eliteBonusViolators1") * level)