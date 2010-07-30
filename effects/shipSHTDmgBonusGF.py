#Variations of item: Atron (3 of 3) [Ship]
#Variations of item: Incursus (3 of 3) [Ship]
#Item: Federation Navy Comet [Ship]
#Item: Helios [Ship]
#Item: Maulus [Ship]
#Item: Tristan [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusGF") * level)