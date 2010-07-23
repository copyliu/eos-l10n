#Item: Rorqual [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Cargo Scanner",
                                  "maxRange", ship.getModifiedItemAttr("cargoScannerRangeBonus"))