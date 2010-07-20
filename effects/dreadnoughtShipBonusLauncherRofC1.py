#Item: Phoenix [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Dreadnought").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Missile Launcher Citadel",
                                  "speed", ship.getModifiedItemAttr("dreadnoughtShipBonusC1") * level)