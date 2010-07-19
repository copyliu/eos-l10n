#Item: Nyx [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Carrier").level
    fit.modules.filteredItemIncrease(lambda mod: mod.group.name == "Gang Coordinator",
                                  "maxGroupActive", ship.getModifiedItemAttr("carrierGallenteBonus4") * level)