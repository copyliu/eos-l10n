#Variations of item: Griffin (2 of 2) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Frigate").level
    for type in ("Gravimetric", "Ladar", "Radar", "Magnetometric"):
        fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                      "scan%sStrengthBonus" % type,
                                      ship.getModifiedItemAttr("shipBonusCF") * level)