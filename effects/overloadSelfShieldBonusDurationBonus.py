#Items from group: Shield Booster (86 of 86) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("duration", module.getModifiedItemAttr("overloadSelfDurationBonus"))
    module.boostItemAttr("shieldBonus", module.getModifiedItemAttr("overloadShieldBonus"))
    