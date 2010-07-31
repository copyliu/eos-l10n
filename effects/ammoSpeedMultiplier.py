#Used by:
#Charges from group: Advanced Artillery Ammo (6 of 6)
#Charges from group: Advanced Autocannon Ammo (6 of 6)
#Charges from group: Advanced Beam Laser Crystal (6 of 6)
#Charges from group: Advanced Blaster Ammo (6 of 6)
#Charges from group: Advanced Pulse Laser Crystal (6 of 6)
#Charges from group: Advanced Railgun Ammo (6 of 6)
#Charges from group: Scanner Probe (7 of 7)
#Charges from group: Survey Probe (3 of 3)
#Charge: Warp Disrupt Probe
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("speed", module.getModifiedChargeAttr("speedMultiplier"))