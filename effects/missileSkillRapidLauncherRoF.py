#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Missile Implants (3 of 6)
#Item: Cerebral Accelerator [Implant]
#Item: Missile Launcher Operation [Skill]
#Item: Rapid Launch [Skill]
#Item: Whelan Machorin's Ballistic Smartlink [Implant]
from customEffects import boostModListBySkillReq
def missileSkillRapidLauncherRoF(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "speed", "rofBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)