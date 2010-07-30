#Item: Wyvern [Ship]
type = "active"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Carrier")
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Gang Coordinator",
                                  "maxGroupActive", ship.getModifiedItemAttr("carrierCaldariBonus4") * level)
