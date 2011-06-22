# Used by:
# Modules from group: Energy Weapon (100 of 183)
# Modules from group: Hybrid Weapon (110 of 199)
# Modules from group: Missile Launcher Citadel (4 of 4)
# Modules from group: Missile Launcher Cruise (20 of 20)
# Modules from group: Missile Launcher Rocket (14 of 14)
# Modules from group: Projectile Weapon (60 of 143)
# Modules named like: Missile Bay (8 of 8)
# Modules named like: Missile Launcher (77 of 78)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("speed", module.getModifiedItemAttr("overloadRofBonus"))
