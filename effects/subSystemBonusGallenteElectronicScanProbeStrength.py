#Item: Proteus Electronics - Emergent Locus Analyzer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Scanner Probe",
                                  "baseSensorStrength", module.getModifiedItemAttr("subsystemBonusGallenteElectronic") * level)