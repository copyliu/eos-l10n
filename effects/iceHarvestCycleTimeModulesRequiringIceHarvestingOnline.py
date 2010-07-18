#Variations of item: Ice Harvester Upgrade I (6 of 6) [Module]
from customEffects import boostModListBySkillReq
import model.fitting

def iceHarvestCycleTimeModulesRequiringIceHarvestingOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(
            fitting.modules,
            "duration",
            "iceHarvestCycleBonus",
            lambda skill: skill.name == "Ice Harvesting",
            self.item
        )
