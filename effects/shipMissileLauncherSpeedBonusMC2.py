#Item: Scythe Fleet Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    groups = ("Missile Launcher Assault", "Missile Launcher Heavy", "Missile Launcher Heavy Assault")
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name in groups,
                                    "speed", ship.getModifiedItemAttr("shipBonusMC2") * level)