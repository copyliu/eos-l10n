#Used by:
#Modules from group: Armor Repair Unit (99 of 99)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("duration", module.getModifiedItemAttr("overloadSelfDurationBonus"))
    module.boostItemAttr("armorDamageAmount", module.getModifiedItemAttr("overloadArmorDamageAmount"))