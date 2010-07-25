#Item: Keres [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Remote Sensor Damper",
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusGF") * level)