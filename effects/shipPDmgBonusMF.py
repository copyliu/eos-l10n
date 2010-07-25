#Variations of item: Rifter (3 of 3) [Ship]
#Variations of item: Slasher (3 of 3) [Ship]
#Item: Cheetah [Ship]
#Item: Republic Fleet Firetail [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusMF") * level)