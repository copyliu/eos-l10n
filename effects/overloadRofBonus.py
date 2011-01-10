#Used by:
#Modules from group: Energy Weapon (99 of 181)
#Modules from group: Hybrid Weapon (109 of 197)
#Modules from group: Missile Launcher Citadel (2 of 2)
#Modules from group: Missile Launcher Cruise (20 of 20)
#Modules from group: Missile Launcher Rocket (14 of 14)
#Modules from group: Projectile Weapon (59 of 141)
#Modules named like: Missile Bay (8 of 8)
#Modules named like: Missile Launcher (77 of 78)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("speed", module.getModifiedItemAttr("overloadRofBonus"))