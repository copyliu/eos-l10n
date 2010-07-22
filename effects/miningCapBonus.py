#Item: Bantam [Ship]
#Item: Burst [Ship]
#Item: Navitas [Ship]
#Item: Tormentor [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Mining Laser",
                                  "capacitorNeed", ship.getModifiedItemAttr("capacitorNeedMultiplier"))