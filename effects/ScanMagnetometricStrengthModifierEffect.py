#Item: Low-grade Spur Alpha [Implant]
#Item: Low-grade Spur Beta [Implant]
#Item: Low-grade Spur Delta [Implant]
#Item: Low-grade Spur Epsilon [Implant]
#Item: Low-grade Spur Gamma [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.increaseItemAttr("scanMagnetometricStrength", implant.getModifiedItemAttr("scanMagnetometricStrengthModifier"))