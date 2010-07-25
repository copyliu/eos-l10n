#Item: Drake [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    for type in ("Em", "Thermal", "Explosive", "Kinetic"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % type, ship.getModifiedItemAttr("shipBonusBC2") * level)