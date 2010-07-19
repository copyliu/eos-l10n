#Item: Hel [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Carrier").level
    fit.modules.filteredItemIncrease(lambda mod: mod.group.name == "Gang Coordinator",
                                     "maxGroupActive", ship.getModifiedItemAttr("carrierMinmatarBonus4") * level)