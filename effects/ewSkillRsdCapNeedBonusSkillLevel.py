#Item: Hardwiring - Zainou 'Gypsy' KRB-25 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KRB-50 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KRB-75 [Implant]
#Item: Sensor Linking [Skill]
from customEffects import boostModListByReq
def ewSkillRsdCapNeedBonusSkillLevel(self, fitting, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)
