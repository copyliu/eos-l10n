#Used by: Item: Signal Distortion Amplifier
from customEffects import boostModListByReq
import model.fitting
def ecmRangeBonusModuleEffect(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "ecmRangeBonus",
                      lambda mod: mod.group.name == "ECM", self.item, useStackingPenalty = True)