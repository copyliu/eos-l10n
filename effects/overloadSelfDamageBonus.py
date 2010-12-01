#Used by:
#Modules from group: Energy Weapon (82 of 181)
#Modules from group: Hybrid Weapon (88 of 197)
#Modules from group: Projectile Weapon (82 of 141)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("damageMultiplier", module.getModifiedItemAttr("overloadDamageModifier"))