#Item: Proteus Electronics - Emergent Locus Analyzer [Subsystem]
from customEffects import boostAmmoListByReq
def subSystemBonusGallenteElectronicScanProbeStrength(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Electronic Systems")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "subsystemBonusGallenteElectronic",
                       lambda mod: mod.group.name == "Scanner Probe",
                       self.item, extraMult = level)