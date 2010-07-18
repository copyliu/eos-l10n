#Items from group: Tracking Link (10 of 10)
type = ("projected", "active")
import model.fitting
from customEffects import boostModListBySkillReq
def targetGunneryMaxRangeFalloffTrackingSpeedBonusAssistance(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowAssistance") != 1:
        boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
        boostModListBySkillReq(fitting.modules, "falloff", "falloffBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
        boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
