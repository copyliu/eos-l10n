#Items from group: Covert Ops (4 of 4)
from customEffects import boostAmmoListByReq
def eliteBonusCoverOpsScanProbeStrength2(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListByReq(fitting.modules, "baseSensorStrength", "eliteBonusCoverOps2",
                       lambda mod: mod.group.name == "Scanner Probe",
                       self.item, extraMult = level)