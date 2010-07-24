#Item: Freki [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Afterburner",
                                    "capacitorNeed", ship.getModifiedItemAttr("shipBonusATF1") * level)