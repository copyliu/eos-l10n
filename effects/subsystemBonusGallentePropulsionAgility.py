#Item: Proteus Propulsion - Interdiction Nullifier [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Propulsion Systems").level
    fit.ship.boostItemAttr("agility", module.getModifiedItemAttr("subsystemBonusGallentePropulsion") * level)