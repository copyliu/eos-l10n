#Item: Information Warfare Link - Electronic Superiority [Module]
type = ("gang", "active")
from customEffects import boostModListByReq
import model.fitting
def commandBonusTPMultiplyWithCommandBonusHidden(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        mult = self.item.getModifiedAttribute("commandBonusHidden")
        boostModListByReq(fitting.modules, "signatureRadiusBonus", "commandBonusTP",
                          lambda mod: mod.group.name == "Target Painter",
                          self.item, useStackingPenalty = True, extraMult = mult)
