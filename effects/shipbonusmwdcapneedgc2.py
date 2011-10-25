# Used by:
# Ships named like: Deimos (2 of 2)
# Ship: Thorax
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
                                     "capacitorCapacityMultiplier", ship.getModifiedItemAttr("shipBonusGC2") * level)
