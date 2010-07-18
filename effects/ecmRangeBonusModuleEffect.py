#Items from group: ECM Stabilizer (6 of 6) [Module]
from customEffects import boostModListByReq
import model.fitting
def ecmRangeBonusModuleEffect(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "ecmRangeBonus",
                      lambda mod: mod.group.name == "ECM", self.item, useStackingPenalty = True)