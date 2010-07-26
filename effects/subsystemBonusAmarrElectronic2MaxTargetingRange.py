#Item: Legion Electronics - Dissolution Sequencer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Electronic Systems").level
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("subsystemBonusAmarrElectronic2") * level)