#Used by: Item: Tracking Enhancer
import model.fitting
from customEffects import boostModListBySkillReq
def gunneryTrackingSpeedBonusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)