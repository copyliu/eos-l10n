#Item: Hardwiring - Eifyr and Co. 'Alchemist' ZA-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' ZA-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Alchemist' ZA-2 [Implant]
from customEffects import boostModListBySkillReq
def gasHarvestingCycleTimeModulesRequiringGasCloudHarvesting(self, fitting):
    boostModListBySkillReq(fitting.modules, "duration", "durationBonus",
                           lambda skill: skill.name == "Gas Cloud Harvesting",
                           self.item)