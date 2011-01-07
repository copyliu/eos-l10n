#Used by:
#Modules from group: Afterburner (107 of 107)
#Modules from group: Capacitor Flux Coil (12 of 12)
#Modules from group: Capacitor Power Relay (25 of 25)
#Modules from group: Power Diagnostic System (31 of 31)
#Modules from group: Reactor Control Unit (28 of 28)
#Modules from group: Shield Flux Coil (11 of 11)
#Modules from group: Shield Power Relay (11 of 11)
#Variations of module: 100MN MicroWarpdrive I (24 of 24)
#Variations of module: 10MN MicroWarpdrive I (14 of 14)
#Variations of module: 1MN MicroWarpdrive I (15 of 15)
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("capacitorCapacity", module.getModifiedItemAttr("capacitorCapacityMultiplier"))
