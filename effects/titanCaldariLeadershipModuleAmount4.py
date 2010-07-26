#Item: Leviathan [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Titan").level
    fit.modules.filteredItemIncrease(lambda mod: mod.group.name == "Gang Coordinator",
                                  "maxGroupActive", ship.getModifiedItemAttr("titanCaldariBonus4") * level)