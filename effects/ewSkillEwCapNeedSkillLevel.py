#Used by: Skill: Electronic Warfare
#       Implant: Hardwiring - Zainou 'Gypsy' KOB series
#        Module: Signal Disruption Amplifier Rigs
from customEffects import boostModListByReq
def ewSkillEwCapNeedSkillLevel(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)
