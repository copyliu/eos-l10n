#Item: Osprey [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Transporter",
                                  "shieldTransferRange", ship.getModifiedItemAttr("maxRangeBonus"))