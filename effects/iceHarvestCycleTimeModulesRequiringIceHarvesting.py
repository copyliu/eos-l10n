#Item: Hardwiring - Inherent Implants 'Yeti' BX-0 [Implant]
#Item: Hardwiring - Inherent Implants 'Yeti' BX-1 [Implant]
#Item: Hardwiring - Inherent Implants 'Yeti' BX-2 [Implant]
#Item: Ice Harvesting [Skill]
#Item: Mackinaw [Ship]
from customEffects import boostModListBySkillReq
def iceHarvestCycleTimeModulesRequiringIceHarvesting(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "iceHarvestCycleBonus",
                           lambda skill: skill.name == "Ice Harvesting",
                           self.item)