#Item: Aeon [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Carrier")
    fit.modules.filteredItemIncrease(lambda mod: mod.item.group.name == "Gang Coordinator",
                                     "maxGroupActive", ship.getModifiedItemAttr("carrierAmarrBonus4") * level)