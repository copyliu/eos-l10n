#Items with name like: Low-grade Harvest (5 of 6)
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Strip Miner",
                                  "maxRange", implant.getModifiedItemAttr("maxRangeBonus"))