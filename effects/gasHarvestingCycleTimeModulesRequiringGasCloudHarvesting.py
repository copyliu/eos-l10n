#Used by: Item: Eifyr & Co 'Alchemist' ZA-X
from customEffects import boostModListBySkillReq
def gasHarvestingCycleTimeModulesRequiringGasCloudHarvesting(self, fitting):
    boostModListBySkillReq(fitting.modules, "duration", "durationBonus",
                           lambda skill: skill.name == "Gas Cloud Harvesting",
                           self.item)