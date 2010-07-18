#Item: Skirmish Warfare Link - Interdiction Maneuvers
from customEffects import boostModListByReq
import model.fitting
type = ("gang", "active")

def gangPropulsionJammingBoost(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "maxRange",
            "commandBonus",
            lambda mod: mod.group.name == "Stasis Web" or mod.group.name == "Warp Scrambler",
            self.item,
            useStackingPenalty = True
        )
