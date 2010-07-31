#Used by:
#Subsystems from group: Electronic Systems (16 of 16)
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("scanGravimetricStrength", module.getModifiedItemAttr("scanGravimetricStrength"))
    fit.ship.increaseItemAttr("scanRadarStrength", module.getModifiedItemAttr("scanRadarStrength"))
    fit.ship.increaseItemAttr("scanMagnetometricStrength", module.getModifiedItemAttr("scanMagnetometricStrength"))
    fit.ship.increaseItemAttr("scanLadarStrength", module.getModifiedItemAttr("scanLadarStrength"))