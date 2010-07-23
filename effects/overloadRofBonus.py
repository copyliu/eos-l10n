#Items from group: Energy Weapon (99 of 181) [Module]
#Items from group: Hybrid Weapon (109 of 197) [Module]
#Items from group: Missile Launcher Assault (12 of 12) [Module]
#Items from group: Missile Launcher Cruise (20 of 20) [Module]
#Items from group: Missile Launcher Heavy (12 of 12) [Module]
#Items from group: Missile Launcher Heavy Assault (12 of 12) [Module]
#Items from group: Missile Launcher Rocket (14 of 14) [Module]
#Items from group: Missile Launcher Siege (21 of 21) [Module]
#Items from group: Projectile Weapon (59 of 141) [Module]
#Items from market group: Ship Equipment > Turrets & Bays > Missile Launchers (44 of 44)
#Items from market group: Ship Equipment > Turrets & Bays > Projectile Turrets > Artillery Cannons (37 of 37)
#Variations of item: Standard Missile Launcher I (12 of 12) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("speed", module.getModifiedItemAttr("overloadRofBonus"))