# Used by:
# Variations of module: 100MN MicroWarpdrive I (24 of 24)
# Variations of module: 10MN MicroWarpdrive I (14 of 14)
# Variations of module: 1MN MicroWarpdrive I (15 of 15)
type = "active"
runTime = "late"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("mass", module.getModifiedItemAttr("massAddition"))
    speedBoost = module.getModifiedItemAttr("speedFactor")
    mass = fit.ship.getModifiedItemAttr("mass")
    thrust = module.getModifiedItemAttr("speedBoostFactor")
    fit.ship.boostItemAttr("maxVelocity", speedBoost * thrust / mass)
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("signatureRadiusBonus"), stackingPenalties = True)
