#Items with name like: Wolf Rayet Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("shieldKineticDamageResonance", beacon.getModifiedItemAttr("shieldKineticDamageResistanceBonus"))