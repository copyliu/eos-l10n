#Used by:
#Charges from group: Advanced Beam Laser Crystal (6 of 6)
#Charges from group: Advanced Blaster Ammo (6 of 6)
#Charges from group: Advanced Pulse Laser Crystal (6 of 6)
#Charges from group: Advanced Railgun Ammo (6 of 6)
#Charges from group: Ammo (128 of 128)
#Items from market group: Ammunition & Charges > Projectile Ammo (140 of 140)
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("trackingSpeed", module.getModifiedChargeAttr("trackingSpeedMultiplier"))