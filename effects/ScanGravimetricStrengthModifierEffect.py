#Item: Low-grade Talon Alpha [Implant]
#Item: Low-grade Talon Beta [Implant]
#Item: Low-grade Talon Delta [Implant]
#Item: Low-grade Talon Epsilon [Implant]
#Item: Low-grade Talon Gamma [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.increaseItemAttr("scanGravimetricStrength", implant.getModifiedItemAttr("scanGravimetricStrengthModifier"))