#Used by:
#Ship: Freki
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Afterburner",
                                    "capacitorNeed", ship.getModifiedItemAttr("shipBonusATF1") * level)