#Item: Tengu Electronics - Dissolution Sequencer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.ship.boostItemAttr("scanGravimetricStrength", module.getModifiedItemAttr("subsystemBonusCaldariElectronic") * level)