#Item: Information Warfare Link - Electronic Superiority [Module]
type = ("gang", "active")
from customEffects import boostModListByReq
import model.fitting
def commandBonusTDMultiplyWithCommandBonusHidden(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        mult = self.item.getModifiedAttribute("commandBonusHidden")
        boostModListByReq(fitting.modules, ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus"),
                          "commandBonusTD", lambda mod: mod.group.name == "Tracking Disruptor",
                          self.item, useStackingPenalty = True, extraMult = mult)
