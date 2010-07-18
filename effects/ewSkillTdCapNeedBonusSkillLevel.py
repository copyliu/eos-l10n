#Item: Weapon Disruption
from customEffects import boostModListByReq
def ewSkillTdCapNeedBonusSkillLevel(self, fitting, level):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)