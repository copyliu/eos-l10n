#Used by:
#Celestials named like: Wolf Rayet Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.ship.boostItemAttr("shieldEmDamageResonance", beacon.getModifiedItemAttr("shieldEmDamageResistanceBonus"))
