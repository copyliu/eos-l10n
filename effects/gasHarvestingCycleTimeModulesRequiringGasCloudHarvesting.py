#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Industry Implants (3 of 9)
from customEffects import boostModListBySkillReq
def gasHarvestingCycleTimeModulesRequiringGasCloudHarvesting(self, fitting):
    boostModListBySkillReq(fitting.modules, "duration", "durationBonus",
                           lambda skill: skill.name == "Gas Cloud Harvesting",
                           self.item)