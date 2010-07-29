#Items from group: Hybrid Weapon (88 of 197) [Module]
#Items from group: Projectile Weapon (82 of 141) [Module]
#Items with name like: Pulse (78 of 84)
#Variations of item: Gatling Pulse Laser I (10 of 10) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("damageMultiplier", module.getModifiedItemAttr("overloadDamageModifier"))