#Variations of item: Maller (2 of 3) [Ship]
#Variations of item: Omen (3 of 3) [Ship]
#Item: Augoror Navy Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusAC") * level)