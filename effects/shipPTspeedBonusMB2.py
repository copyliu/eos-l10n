#Used by:
#Variations of ship: Tempest (4 of 4)
#Variations of ship: Typhoon (3 of 3)
#Ship: Maelstrom
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusMB2") * level)