#Used by: Skill: Projected Electronic Couter Measures
from customEffects import boostModListByReq
def skillRemoteECMDurationBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "duration", "projECMDurationBonus",
                      lambda mod: mod.group.name == "Remote ECM Burst",
                      self.item, extraMult = level)