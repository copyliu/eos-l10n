#Items from group: Electronic Systems (16 of 16) [Subsystem]
type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("scanGravimetricStrength", module.getModifiedItemAttr("scanGravimetricStrength"))
    fit.ship.increaseItemAttr("scanRadarStrength", module.getModifiedItemAttr("scanRadarStrength"))
    fit.ship.increaseItemAttr("scanMagnetometricStrength", module.getModifiedItemAttr("scanMagnetometricStrength"))
    fit.ship.increaseItemAttr("scanLadarStrength", module.getModifiedItemAttr("scanLadarStrength"))