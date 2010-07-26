#Item: Legion Electronics - Emergent Locus Analyzer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Scanner Probe",
                                  "baseSensorStrength", module.getModifiedItemAttr("subsystemBonusAmarrElectronic") * level)