#Used by:
#Ship: Blackbird
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    for type in ("Gravimetric", "Magnetometric", "Ladar", "Radar"):
        fit.drones.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                     "scan%sStrengthBonus" % type, ship.getModifiedItemAttr("shipBonusGC2") * level)