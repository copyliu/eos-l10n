#Item: Probe
from customEffects import boostAmmoListByReq
def shipBonusScanProbeStrengthMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "shipBonusMF2",
                       lambda charge: charge.group.name == "Scanner Probe",
                       self.item, extraMult = level)