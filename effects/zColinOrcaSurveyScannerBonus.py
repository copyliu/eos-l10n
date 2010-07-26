#Item: Orca [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Survey Scanner",
                                  "maxRange", ship.getModifiedItemAttr("shipOrcaSurveyScannerBonus"))