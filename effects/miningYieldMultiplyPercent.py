#Used by: Item: Mining Laser Upgrade
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
