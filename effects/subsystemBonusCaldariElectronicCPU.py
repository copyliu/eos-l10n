#Item: Tengu Electronics - CPU Efficiency Gate [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("subsystemBonusCaldariElectronic") * level)
