#Items from group: Advanced Artillery Ammo (6 of 6) [Charge]
#Items from group: Advanced Autocannon Ammo (6 of 6) [Charge]
#Items from group: Advanced Beam Laser Crystal (6 of 6) [Charge]
#Items from group: Advanced Blaster Ammo (6 of 6) [Charge]
#Items from group: Advanced Pulse Laser Crystal (6 of 6) [Charge]
#Items from group: Advanced Railgun Ammo (6 of 6) [Charge]
#Items from market group: Ammunition & Charges > Probes (11 of 11)
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("speed", module.getModifiedChargeAttr("speedMultiplier"))