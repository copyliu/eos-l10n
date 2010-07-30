#Item: Utu [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: "heatDamage" in mod.itemModifiedAttributes,
                                    "heatDamage", ship.getModifiedItemAttr("shipBonusATF1"))