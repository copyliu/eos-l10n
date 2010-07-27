#Item: Scorpion [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    for sensorType in ("Gravimetric", "Ladar", "Magnetometric", "Radar"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                      "scan%sStrengthBonus" % sensorType,
                                      ship.getModifiedItemAttr("shipBonusCB") * level)