#Item: Augoror [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Transfer Array",
                                  "powerTransferRange", ship.getModifiedItemAttr("maxRangeBonus"))