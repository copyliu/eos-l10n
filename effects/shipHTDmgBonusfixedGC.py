#Variations of item: Celestis (3 of 3) [Ship]
#Variations of item: Thorax (3 of 4) [Ship]
#Variations of item: Vexor (4 of 4) [Ship]
#Item: Adrestia [Ship]
#Item: Exequror Navy Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusGC") * level)