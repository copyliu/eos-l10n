#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPZ-1 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Data Miners",
                                  "duration", implant.getModifiedItemAttr("durationBonus"))