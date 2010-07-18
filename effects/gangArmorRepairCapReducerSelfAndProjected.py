#Item: Armored Warfare Link - Damage Control [Module]
import model.fitting
from customEffects import boostModListByReq

type = ("gang", "active")

def gangArmorRepairCapReducerSelfAndProjected(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "capacitorNeed",
            "commandBonus",
            lambda mod: mod.group.name == "Armor Repair Unit" or mod.group.name == "Armor Repair Projector",
            self.item,
            useStackingPenalty = True
        )
