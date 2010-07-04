#Used by: Item: Mining Laser Upgrade
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
