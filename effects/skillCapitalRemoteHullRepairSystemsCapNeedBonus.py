#Used by: Skill: Capital Remote Hull Repair Systems
from customEffects import boostModListByReq
def skillCapitalRemoteHullRepairSystemsCapNeedBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)