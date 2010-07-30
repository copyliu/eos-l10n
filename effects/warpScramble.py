#Items with name like: Warp Disruptor (20 of 20)
#Variations of item: Warp Disruptor I (18 of 18) [Module]
type = "projected", "active"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))