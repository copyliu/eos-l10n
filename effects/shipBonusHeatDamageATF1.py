#Used by:
#Ship: Utu
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: True, "heatDamage",
                                  ship.getModifiedItemAttr("shipBonusATF1"))
