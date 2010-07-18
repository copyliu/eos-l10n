#Items from group: Cyber Electronics (6 of 27)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Electronics Implants (6 of 12)
#Item: Target Painting
from customEffects import boostModListByReq
def ewSkillTpCapNeedBonusSkillLevel(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)