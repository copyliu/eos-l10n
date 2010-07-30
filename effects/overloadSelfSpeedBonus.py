#Items from group: Afterburner (107 of 107) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("speedFactor", module.getModifiedItemAttr("overloadSpeedFactorBonus"))