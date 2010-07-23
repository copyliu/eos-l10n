#Items from group: Capacitor Flux Coil (12 of 12) [Module]
#Items from group: Capacitor Power Relay (25 of 25) [Module]
#Items from group: Capacitor Recharger (25 of 25) [Module]
#Items from group: Power Diagnostic System (31 of 31) [Module]
#Items from group: Reactor Control Unit (28 of 28) [Module]
#Items from group: Shield Flux Coil (11 of 11) [Module]
#Items from group: Shield Power Relay (11 of 11) [Module] 
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("rechargeRate", module.getModifiedItemAttr("capacitorRechargeRateMultiplier"))