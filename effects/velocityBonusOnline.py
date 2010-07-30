#Items from group: Nanofiber Internal Structure (14 of 14) [Module]
#Items from group: Overdrive Injector System (14 of 14) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("implantBonusVelocity"),
                           stackingPenalties = True)