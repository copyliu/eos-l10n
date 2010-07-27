#Item: Guardian [Ship]
#Item: Oneiros [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Projector",
                                  "power", ship.getModifiedItemAttr("remoteArmorPowerNeedBonus"))