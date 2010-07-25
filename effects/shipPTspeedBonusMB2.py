#Variations of item: Tempest (4 of 4) [Ship]
#Variations of item: Typhoon (3 of 3) [Ship]
#Item: Maelstrom [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusMB2") * level)