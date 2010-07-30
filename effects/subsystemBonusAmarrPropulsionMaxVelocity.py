#Item: Legion Propulsion - Chassis Optimization [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Propulsion Systems").level
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("subsystemBonusAmarrPropulsion") * level)
