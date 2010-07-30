#Item: Loki Electronics - Dissolution Sequencer [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Electronic Systems").level
    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("subsystemBonusMinmatarElectronic2") * level)
