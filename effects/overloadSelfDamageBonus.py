#Items from group: Energy Weapon (82 of 181) [Module]
#Items from group: Hybrid Weapon (88 of 197) [Module]
#Items from group: Projectile Weapon (82 of 141) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("damageMultiplier", module.getModifiedItemAttr("overloadDamageModifier"))