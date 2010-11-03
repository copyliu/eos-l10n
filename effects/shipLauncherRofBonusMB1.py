#Used by:
#Ships named like: Typhoon (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battleship").level
    groups = ("Missile Launcher Siege", "Missile Launcher Cruise")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "speed", ship.getModifiedItemAttr("shipBonusMB") * level)
