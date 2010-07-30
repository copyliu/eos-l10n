#Item: Loki Propulsion - Chassis Optimization [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Propulsion Systems").level
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("subsystemBonusMinmatarPropulsion") * level)
