#Used by: Ship: Helios
#               Cheetah
#               Anathema
#               Buzzard
from customEffects import boostAmmoListByReq
def eliteBonusCoverOpsScanProbeStrength2(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "eliteBonusCoverOps2",
                       lambda mod: mod.group.name == "Scanner Probe",
                       self.item, extraMult = level)