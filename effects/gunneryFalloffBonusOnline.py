#Items from group: Tracking Enhancer (17 of 17) [Module]
import model.fitting
from customEffects import boostModListBySkillReq
def gunneryFalloffBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(fitting.modules, "falloff", "falloffBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
