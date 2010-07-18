#Item: Capital Energy Emission Systems [Skill]
from customEffects import boostModListByReq
def capitalRemoteEnergyTransferCapNeedBonusSkill(self, fitting, level):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)