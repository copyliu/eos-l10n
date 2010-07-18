#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Industry Implants (3 of 9)
#Item: Ice Harvesting
#Item: Mackinaw
from customEffects import boostModListBySkillReq
def iceHarvestCycleTimeModulesRequiringIceHarvesting(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "iceHarvestCycleBonus",
                           lambda skill: skill.name == "Ice Harvesting",
                           self.item)