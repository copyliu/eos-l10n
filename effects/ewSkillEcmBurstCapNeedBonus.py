#Used by: Skill: Electronic Warfare
#       Implant: Hardwiring - Zainou 'Gypsy' KOB series
#        Module: Signal Disruption Amplifier Rigs
from customEffects import boostModListByReq
def ewSkillEcmBurstCapNeedBonus(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "ECM Burst",
                      self.item, extraMult = level)
