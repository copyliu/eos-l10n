#Item: Basilisk [Ship]
#Item: Scimitar [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Transporter",
                                  "cpu", ship.getModifiedItemAttr("shieldTransportCpuNeedBonus"))