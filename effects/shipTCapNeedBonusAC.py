#Used by:
#Variations of ship: Maller (2 of 3)
#Variations of ship: Omen (3 of 3)
#Ship: Augoror Navy Issue
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusAC") * level)