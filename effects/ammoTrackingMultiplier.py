# Used by:
# Charges from group: Advanced Artillery Ammo (6 of 6)
# Charges from group: Advanced Autocannon Ammo (6 of 6)
# Charges from group: Advanced Beam Laser Crystal (6 of 6)
# Charges from group: Advanced Blaster Ammo (6 of 6)
# Charges from group: Advanced Pulse Laser Crystal (6 of 6)
# Charges from group: Advanced Railgun Ammo (6 of 6)
# Charges from group: Projectile Ammo (128 of 128)
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("trackingSpeed", module.getModifiedChargeAttr("trackingSpeedMultiplier"))