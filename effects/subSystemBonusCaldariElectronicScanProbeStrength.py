#Item: Tengu Electronics - Emergent Locus Analyzer [Subsystem]
from customEffects import boostAmmoListByReq
def subSystemBonusCaldariElectronicScanProbeStrength(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Electronic Systems")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "subsystemBonusCaldariElectronic",
                       lambda mod: mod.group.name == "Scanner Probe",
                       self.item, extraMult = level)