#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Missile Implants (3 of 6)
#Item: Cerebral Accelerator
#Item: Missile Launcher Operation
#Item: Rapid Launch
#Item: Whelan Machorin's Ballistic Smartlink
from customEffects import boostModListBySkillReq
def missileSkillRapidLauncherRoF(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "speed", "rofBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)