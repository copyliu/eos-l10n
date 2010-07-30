#Used by:
#Subsystem: Tengu Electronics - Emergent Locus Analyzer
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Scanner Probe",
                                  "baseSensorStrength", module.getModifiedItemAttr("subsystemBonusCaldariElectronic") * level)
