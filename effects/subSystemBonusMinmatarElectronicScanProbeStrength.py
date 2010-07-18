#Item: Loki Electronics - Emergent Locus Analyzer
from customEffects import boostAmmoListByReq
def subSystemBonusMinmatarElectronicScanProbeStrength(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "subsystemBonusMinmatarElectronic",
                       lambda mod: mod.group.name == "Scanner Probe",
                       self.item, extraMult = level)