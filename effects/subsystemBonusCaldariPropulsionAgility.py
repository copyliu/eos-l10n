#Item: Tengu Propulsion - Intercalated Nanofibers [Subsystem]
#Item: Tengu Propulsion - Interdiction Nullifier [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Propulsion Systems").level
    fit.ship.boostItemAttr("agility", module.getModifiedItemAttr("subsystemBonusCaldariPropulsion") * level)
