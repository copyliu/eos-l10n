#Variations of item: Mining Laser Upgrade I (6 of 6) [Module]
from customEffects import boostModListBySkillReq
import model.fitting

def miningYieldMultiplyPercent(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(
            fitting.modules,
            "miningAmount",
            "miningAmountBonus",
            lambda skill: skill.name == "Mining",
            self.item
        )
