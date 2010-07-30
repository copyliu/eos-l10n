#Item: Stabber Fleet Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                    "trackingSpeed", ship.getModifiedItemAttr("shipBonusMC2") * level)