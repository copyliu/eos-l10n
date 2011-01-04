#Used by:
#Variations of module: Warp Disruptor I (18 of 18)
#Module: Civilian Warp Disruptor
type = "projected", "active"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))