#Item: Loki Electronics - Emergent Locus Analyzer [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Scanner Probe",
                                  "baseSensorStrength", module.getModifiedItemAttr("subsystemBonusMinmatarElectronic") * level)
