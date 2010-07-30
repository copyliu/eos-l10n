#Variations of item: Bellicose (3 of 3) [Ship]
#Variations of item: Rupture (3 of 3) [Ship]
#Variations of item: Stabber (3 of 3) [Ship]
#Item: Scythe Fleet Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusMC") * level)