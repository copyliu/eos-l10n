#Used by:
#Ship: Adrestia
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Warp Scrambler",
                                    "maxRange", ship.getModifiedItemAttr("shipBonusGC2") * level)