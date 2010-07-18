#Items from group: Cyber Armor (3 of 24) [Implant]
#Item: Capital Remote Armor Repair Systems [Skill]
from customEffects import boostModListByReq
def capitalRemoteArmorRepairerCapNeedBonusSkill(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)