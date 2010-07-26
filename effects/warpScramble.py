#Items from group: Warp Scrambler (20 of 39) [Module]
#Variations of item: Warp Disruptor I (18 of 18) [Module]
type = "projected", "active"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))