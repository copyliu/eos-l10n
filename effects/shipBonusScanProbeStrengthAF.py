#Item: Magnate
from customEffects import boostAmmoListByReq
def shipBonusScanProbeStrengthAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "shipBonus2AF",
                       lambda charge: charge.group.name == "Scanner Probe",
                       self.item, extraMult = level)