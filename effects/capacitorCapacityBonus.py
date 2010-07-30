#Items from group: Capacitor Battery (27 of 27) [Module]
type = "passive"
def handler(fit, ship, context):
    fit.ship.increaseItemAttr("capacitorCapacity", ship.getModifiedItemAttr("capacitorBonus"))