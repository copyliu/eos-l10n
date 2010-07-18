#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Electronics Implants (3 of 12)
#Item: Sensor Linking [Skill]
from customEffects import boostModListByReq
def ewSkillRsdCapNeedBonusSkillLevel(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)
