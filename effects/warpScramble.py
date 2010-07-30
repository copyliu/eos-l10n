#Used by:
#Modules named like: Warp Disruptor (20 of 20)
#Variations of module: Warp Disruptor I (18 of 18)
type = "projected", "active"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))