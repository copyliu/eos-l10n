#Used by: Skill: Capital Remote Armor Repair Systems
from customEffects import boostModListByReq
def capitalRemoteArmorRepairerCapNeedBonusSkill(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)