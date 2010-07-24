#Item: Scythe [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.group.name == "Tracking Link",
                                    "trackingSpeedBonus", ship.getModifiedItemAttr("shipBonusMC") * level)