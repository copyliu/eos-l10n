#Items from group: Stasis Web (19 of 19) [Module]
#Items from group: Warp Scrambler (38 of 39) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("maxRange", module.getModifiedItemAttr("overloadRangeBonus"),
                         stackingPenalties = True)