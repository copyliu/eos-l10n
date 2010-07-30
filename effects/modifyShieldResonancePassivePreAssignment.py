#Items from group: Defensive Systems (16 of 16) [Subsystem]
type = "passive"
def handler(fit, module, context):
    for type in ("Em", "Kinetic", "Thermal", "Explosive"):
        fit.ship.multiplyItemAttr("shield%sDamageResonance" % type,
                                  module.getModifiedItemAttr("passiveArmor%sDamageResonance" % type))
