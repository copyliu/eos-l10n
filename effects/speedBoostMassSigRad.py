#Items from group: Afterburner (53 of 107) [Module]
type = "active"
runTime = "late"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("mass", module.getModifiedItemAttr("massAddition"))
    mass = module.getModifiedItemAttr("mass")
    thrust = module.getModifiedItemAttr("speedBoostFactor")
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor") * thrust / mass)
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("signatureRadiusBonus"))