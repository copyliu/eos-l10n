#Item: Low-grade Grail Alpha [Implant]
#Item: Low-grade Grail Beta [Implant]
#Item: Low-grade Grail Delta [Implant]
#Item: Low-grade Grail Epsilon [Implant]
#Item: Low-grade Grail Gamma [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.increaseItemAttr("scanRadarStrength", implant.getModifiedItemAttr("scanRadarStrengthModifier"))