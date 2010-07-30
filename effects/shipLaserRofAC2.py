#Used by:
#Variations of ship: Omen (3 of 3)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusAC2") * level)