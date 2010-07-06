#Used by: Ship: Imicus
from customEffects import boostAmmoListByReq
def shipBonusScanProbeStrengthGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "shipBonusGF2",
                       lambda charge: charge.group.name == "Scanner Probe",
                       self.item, extraMult = level)