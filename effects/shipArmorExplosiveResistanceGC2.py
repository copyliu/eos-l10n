#Item: Phobos [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.ship.boostItemAttr("armorExplosiveDamageResonance", ship.getModifiedItemAttr("shipBonusGC2") * level)