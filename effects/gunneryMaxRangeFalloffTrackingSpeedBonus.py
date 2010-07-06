#Used by: Item: Tracking Computer
import model.fitting
from customEffects import boostModListBySkillReq
type = "active"
def gunneryMaxRangeFalloffTrackingSpeedBonus(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
        boostModListBySkillReq(fitting.modules, "falloff", "falloffBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
        boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
