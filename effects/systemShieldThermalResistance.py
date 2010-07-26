#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("shieldThermalDamageResonance", beacon.getModifiedItemAttr("shieldThermalDamageResistanceBonus"))