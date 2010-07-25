#Variations of item: Slasher (2 of 3) [Ship]
#Item: Republic Fleet Firetail [Ship]
#Item: Rifter [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("shipBonusMF2") * level)