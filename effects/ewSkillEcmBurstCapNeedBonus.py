#Items from group: Rig Electronics (6 of 30) [Module]
#Item: Electronic Warfare [Skill]
#Item: Hardwiring - Zainou 'Gypsy' KOB-25 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KOB-50 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KOB-75 [Implant]
from customEffects import boostModListByReq
def ewSkillEcmBurstCapNeedBonus(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "ECM Burst",
                      self.item, extraMult = level)
