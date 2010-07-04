#Used by: Item: Information Warfare Link - Electronic Superiority
type = ("gang", "active")
from customEffects import boostModListByReq
import model.fitting
def commandBonusECMMultiplyWithCommandBonusHidden(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        mult = self.item.getModifiedAttribute("commandBonusHidden")
        boostModListByReq(fitting.modules,
                          ("scanMagnetometricStrengthBonus", "scanRadarStrengthBonus",
                           "scanLadarStrengthBonus", "scanGravimetricStrengthBonus"),
                          "commandBonusECM", lambda mod: mod.group.name == "ECM",
                          self.item, useStackingPenalty = True, extraMult = mult)
