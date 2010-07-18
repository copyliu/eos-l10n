#Item: Armored Warfare Link - Rapid Repair
import model.fitting
from customEffects import boostModListByReq
type = ("gang", "active")

def gangArmorRepairSpeedAmplifierSelfAndProjected(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "duration",
            "commandBonus",
            lambda mod: mod.group.name == "Armor Repair Unit" or mod.group.name == "Armor Repair Projector",
            self.item,
            useStackingPenalty = True
        )
