#Used by: Ship : Mackinaw
#         Item : Hardwiring - Inherent Implant 'Yeti'
#         Skill: Ice Harvesting
from customEffects import boostModListBySkillReq
def iceHarvestCycleTimeModulesRequiringIceHarvesting(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "iceHarvestCycleBonus",
                           lambda skill: skill.name == "Ice Harvesting",
                           self.item)