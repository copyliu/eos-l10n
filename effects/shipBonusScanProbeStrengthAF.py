#Used by: Ship: Magnate
from customEffects import boostAmmoListByReq
def shipBonusScanProbeStrengthAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "shipBonus2AF",
                       lambda ammo: ammo.group.name == "Scanner Probe",
                       self.item, extraMult = level)