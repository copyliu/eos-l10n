#Items from category: Charge (164 of 814)
#Items from group: Ammo (128 of 128) [Charge]
#Items from market group: Ammunition & Charges > Projectile Ammo (140 of 140)
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("trackingSpeed", module.getModifiedChargeAttr("trackingSpeedMultiplier"))