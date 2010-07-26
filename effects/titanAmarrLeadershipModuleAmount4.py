#Item: Avatar [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Titan").level
    fit.modules.filteredItemIncrease(lambda mod: mod.group.name == "Gang Coordinator",
                                  "maxGroupActive", ship.getModifiedItemAttr("titanAmarrBonus4") * level)