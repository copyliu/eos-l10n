#Used by:
#Ship: Basilisk
#Ship: Scimitar
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Transporter",
                                  "cpu", ship.getModifiedItemAttr("shieldTransportCpuNeedBonus"))
