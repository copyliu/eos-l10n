#Item: Capital Remote Armor Repair Systems [Skill]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX20 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX200 [Implant]
#Item: Hardwiring - Inherent Implants 'Gentry' ZEX2000 [Implant]
from customEffects import boostModListByReq
def capitalRemoteArmorRepairerCapNeedBonusSkill(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)