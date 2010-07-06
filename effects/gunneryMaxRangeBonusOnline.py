#Used by: Item: Tracking Enhancer
import model.fitting
from customEffects import boostModListBySkillReq
def gunneryMaxRangeBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)