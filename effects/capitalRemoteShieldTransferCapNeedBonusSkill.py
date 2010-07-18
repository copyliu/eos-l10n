#Items from group: Cyber Engineering (3 of 21)
#Item: Capital Shield Emission Systems
from customEffects import boostModListByReq
def capitalRemoteShieldTransferCapNeedBonusSkill(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)