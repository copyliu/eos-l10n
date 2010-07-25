#Item: Navitas [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Mining Laser",
                                  "miningAmount", ship.getModifiedItemAttr("shipBonusGF") * level)