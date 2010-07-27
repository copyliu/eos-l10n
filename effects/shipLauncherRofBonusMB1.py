#Variations of item: Typhoon (2 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Destroyers").level
    groups = "Missile Launcher Siege", "Missile Launcher Cruise"
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "speed", ship.getModifiedItemAttr("shipBonusMB") * level)