#Item: Oneiros [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Logistics").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Link",
                                  "falloffBonus", ship.getModifiedItemAttr("eliteBonusLogistics2") * level)