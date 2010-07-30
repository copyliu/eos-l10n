#Used by:
#Modules from group: Energy Weapon (99 of 181)
#Modules from group: Hybrid Weapon (109 of 197)
#Modules from group: Missile Launcher Rocket (14 of 14)
#Modules from group: Projectile Weapon (59 of 141)
#Modules named like: Missile Launcher (77 of 78)
#Items from market group: Ship Equipment > Turrets & Bays > Missile Launchers (44 of 44)
#Items from market group: Ship Equipment > Turrets & Bays > Projectile Turrets > Artillery Cannons (37 of 37)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("speed", module.getModifiedItemAttr("overloadRofBonus"))