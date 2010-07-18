type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("warmScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))