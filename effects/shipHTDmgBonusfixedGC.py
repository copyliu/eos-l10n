#Used by:
#Variations of ship: Celestis (3 of 3)
#Variations of ship: Thorax (3 of 4)
#Variations of ship: Vexor (4 of 4)
#Ship: Adrestia
#Ship: Exequror Navy Issue
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusGC") * level)