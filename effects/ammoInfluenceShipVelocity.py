#Items from market group: Ammunition & Charges > Hybrid Charges > Advanced Railgun Charges (6 of 6)
#Items from market group: Ammunition & Charges > Missiles > Cruise Missiles > Advanced High Precision Cruise Missiles (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Heavy Assault Missiles > Advanced Long Range Assault Missiles (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Heavy Missiles > Advanced High Precision Heavy Missiles (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Light Missiles > Advanced High Precision Light Missiles (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Rockets > Advanced Long Range Rockets (4 of 4)
#Items from market group: Ammunition & Charges > Missiles > Torpedoes > Advanced Long Range Torpedoes (4 of 4)
#Items from market group: Ammunition & Charges > Projectile Ammo > Advanced Artillery Ammo (6 of 6)
#Items from market group: Ammunition & Charges > Projectile Ammo > Advanced Autocannon Ammo (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxVelocity", module.getModifiedChargeAttr("maxVelocityBonus"))