#Item: Utu [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Warp Scrambler",
                                    "maxRange", ship.getModifiedItemAttr("shipBonusGF2") * level)