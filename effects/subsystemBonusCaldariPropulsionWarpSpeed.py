#Item: Tengu Propulsion - Gravitational Capacitor [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Propulsion Systems").level
    fit.ship.boostItemAttr("baseWarpSpeed", module.getModifiedItemAttr("subsystemBonusCaldariPropulsion") * level)
