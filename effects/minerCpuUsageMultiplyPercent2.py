#Variations of item: Mining Laser Upgrade I (6 of 6)
from customEffects import boostModListBySkillReq
import model.fitting
def minerCpuUsageMultiplyPercent2(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(
            fitting.modules,
            "cpu",
            "cpuPenaltyPercent",
            lambda skill: skill.name == "Mining",
            self.item
        )
