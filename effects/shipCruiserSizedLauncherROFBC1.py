#Item: Nighthawk [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    groups = "Missile Launcher Assault", "Missile Launcher Heavy", "Missile Launcher Heavy Assault"
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name in groups,
                                    "speed", ship.getModifiedItemAttr("shipBonusBC1") * level)