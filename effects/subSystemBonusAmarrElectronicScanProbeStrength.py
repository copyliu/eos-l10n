#Item: Legion Electronics - Emergent Locus Analyzer [Subsystem]
from customEffects import boostAmmoListByReq
def subSystemBonusAmarrElectronicScanProbeStrength(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "subsystemBonusAmarrElectronic",
                       lambda mod: mod.group.name == "Scanner Probe",
                       self.item, extraMult = level)