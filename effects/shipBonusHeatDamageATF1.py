#Used by:
#Ship: Utu
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: "heatDamage" in mod.itemModifiedAttributes,
                                  "heatDamage", ship.getModifiedItemAttr("shipBonusATF1"))
