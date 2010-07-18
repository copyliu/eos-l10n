#Item: Capital Shield Operation
from customEffects import boostModListByReq
def capitalShieldOperationSkillCapacitorNeedBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)