#Item: Adrestia [Ship]
#Item: Mimir [Ship]
type = "passive"
def handler(fit, ship, context):
    fit.ship.boostItemAttr("maxVelocity", ship.getModifiedItemAttr("shipBonusATC1"))