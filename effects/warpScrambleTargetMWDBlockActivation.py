#Variations of item: Warp Scrambler I (19 of 19) [Module]
runTime = "early"
type = "projected", "active"
def handler(fit, module, context):
    if "projected" not in context or fit.ship.getModifiedItemAttr("disallowOffensiveModifiers") == 1:
        return

    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))
    for module in fit.modules:
        if module.item.requiresSkill("High Speed Maneuvering"):
            module.block()
