#Used by:
#Ship: Basilisk
#Ship: Guardian
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Transfer Array",
                                  "power", ship.getModifiedItemAttr("powerTransferPowerNeedBonus"))
