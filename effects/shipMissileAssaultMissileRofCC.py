#Item: Osprey Navy Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Missile Launcher Assault",
                                    "speed", ship.getModifiedItemAttr("shipBonusCC") * level)