#Item: Capital Repair Systems [Skill]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX10 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX100 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX1000 [Implant]
from customEffects import boostModListByReq
def capitalRepairSystemsSkillDurationBonus(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)