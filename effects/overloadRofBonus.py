#Items from group: Energy Weapon (99 of 181) [Module]
#Items from group: Hybrid Weapon (109 of 197) [Module]
#Items from group: Missile Launcher Rocket (14 of 14) [Module]
#Items from group: Projectile Weapon (59 of 141) [Module]
#Items with name like: Missile Launcher (77 of 79)
#Items from market group: Ship Equipment > Turrets & Bays > Missile Launchers (44 of 44)
#Items from market group: Ship Equipment > Turrets & Bays > Projectile Turrets > Artillery Cannons (37 of 37)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("speed", module.getModifiedItemAttr("overloadRofBonus"))