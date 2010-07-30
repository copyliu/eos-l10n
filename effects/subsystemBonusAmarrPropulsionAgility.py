#Item: Legion Propulsion - Interdiction Nullifier [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Propulsion Systems").level
    fit.ship.boostItemAttr("agility", module.getModifiedItemAttr("subsystemBonusAmarrPropulsion") * level)
