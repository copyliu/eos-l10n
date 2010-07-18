#Variations of item: Ice Harvester Upgrade I (6 of 6)
from customEffects import boostModListBySkillReq
import model.fitting
def iceMinerCpuUsagePercent(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(
            fitting.modules,
            "cpu",
            "cpuPenaltyPercent",
            lambda skill: skill.name == "Ice Harvesting",
            self.item
        )
