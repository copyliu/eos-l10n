#Items from group: Afterburner (54 of 107) [Module]
#Items with name like: Afterburner (47 of 48)
type = "active"
runTime = "late"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("mass", module.getModifiedItemAttr("massAddition"))
    mass = module.getModifiedItemAttr("mass")
    thrust = module.getModifiedItemAttr("speedBoostFactor")
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor") * thrust / mass)