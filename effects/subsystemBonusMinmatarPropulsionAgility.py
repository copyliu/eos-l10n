#Item: Loki Propulsion - Intercalated Nanofibers [Subsystem]
#Item: Loki Propulsion - Interdiction Nullifier [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Propulsion Systems").level
    fit.ship.boostItemAttr("agility", module.getModifiedItemAttr("subsystemBonusMinmatarPropulsion") * level)