#Item: Siege Warfare Link - Active Shielding
from customEffects import boostModListByReq
import model.fitting
type = ("gang", "active")

def gangShieldBoosterAndTransporterSpeed(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "duration",
            "commandBonus",
            lambda mod: mod.group.name == "Shield Booster" or mod.group.name == "Shield Transporter",
            self.item,
            useStackingPenalty = True
        )
