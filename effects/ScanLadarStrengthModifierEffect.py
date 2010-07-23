#Item: Low-grade Jackal Alpha [Implant]
#Item: Low-grade Jackal Beta [Implant]
#Item: Low-grade Jackal Delta [Implant]
#Item: Low-grade Jackal Epsilon [Implant]
#Item: Low-grade Jackal Gamma [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.increaseItemAttr("scanLadarStrength", implant.getModifiedItemAttr("scanLadarStrengthModifier"))