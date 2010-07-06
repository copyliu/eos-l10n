#Used by: Skill: Propulsion Jamming
from customEffects import boostModListByReq
def propulsionSkillCapNeedBonusSkillLevel(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Stasis Web" or mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)