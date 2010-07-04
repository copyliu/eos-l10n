#Used by: Skill: Missile Launcher Operation
#                Rapid Launch
from customEffects import boostModListBySkillReq
def missileSkillRapidLauncherRoF(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "speed", "rofBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)