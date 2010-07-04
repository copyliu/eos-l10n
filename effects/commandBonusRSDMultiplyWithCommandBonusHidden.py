#Used by: Item: Information Warfare Link - Electronic Superiority
type = ("gang", "active")
from customEffects import boostModListByReq
import model.fitting
def commandBonusRSDMultiplyWithCommandBonusHidden(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        mult = self.item.getModifiedAttribute("commandBonusHidden")
        boostModListByReq(fitting.modules, ("scanResolutionBonus", "maxTargetRangeBonus"),
                          "commandBonusRSD", lambda mod: mod.group.name == "Remote Sensor Damper",
                          self.item, useStackingPenalty = True, extraMult = mult)
