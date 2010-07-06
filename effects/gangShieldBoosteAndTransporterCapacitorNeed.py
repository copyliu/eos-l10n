#Used by: Item: Siege Warfare Link - Shield Efficiency
from customEffects import boostModListByReq
import model.fitting
type = ("gang", "active")

def gangShieldBoosteAndTransporterCapacitorNeed(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "capacitorNeed",
            "commandBonus",
            lambda mod: mod.group.name == "Shield Booster" or mod.group.name == "Shield Transporter",
            self.item,
            useStackingPenalty = True
        )
