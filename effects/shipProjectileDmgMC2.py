#Variations of item: Rupture (2 of 3) [Ship]
#Item: Cynabal [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusMC2") * level)