#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Electronics Implants (3 of 6)
#Item: Propulsion Jamming [Skill]
from customEffects import boostModListByReq
def propulsionSkillCapNeedBonusSkillLevel(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Stasis Web" or mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)