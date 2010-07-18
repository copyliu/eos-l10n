#Items from group: Tracking Disruptor (10 of 10) [Module]
import model.fitting
from customEffects import boost, boostModListBySkillReq
type = ("projected", "active")
def targetGunneryMaxRangeAndTrackingSpeedAndFalloffBonusHostile(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowOffensiveModifiers") != 1:
        boostModListBySkillReq(fitting.modules, "trackingSpeed", "trackingSpeedBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
        boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)
        boostModListBySkillReq(fitting.modules, "falloff", "falloffBonus",
                               lambda skill: skill.name == "Gunnery",
                               self.item, useStackingPenalty = True)