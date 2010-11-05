#Used by:
#Ship: Osprey
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Transporter",
                                  "shieldTransferRange", ship.getModifiedItemAttr("maxRangeBonus"))
