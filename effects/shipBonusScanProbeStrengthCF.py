#Item: Heron
from customEffects import boostAmmoListByReq
def shipBonusScanProbeStrengthCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "shipBonusCF2",
                       lambda charge: charge.group.name == "Scanner Probe",
                       self.item, extraMult = level)