#Items from group: Force Recon Ship (4 of 4) [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Cynosural Field",
                                  "duration", ship.getModifiedItemAttr("durationBonus"))