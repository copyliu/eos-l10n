#Used by: Item: Skirmish Warfare Link - Rapid Deployment
import model.fitting
from customEffects import boostModListByReq
type = ("gang", "active")

def gangAbMwdFactorBoost(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "speedFactor",
            "commandBonus",
            lambda mod: mod.group.name == "Afterburner",
            self.item,
            useStackingPenalty = True
        )
