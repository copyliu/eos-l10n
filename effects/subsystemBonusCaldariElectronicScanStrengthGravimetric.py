#Item: Tengu Electronics - Dissolution Sequencer [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.ship.boostItemAttr("scanGravimetricStrength", module.getModifiedItemAttr("subsystemBonusCaldariElectronic") * level)
