#Used by: Item: Mining Foreman Link - Laser Optimization
import model.fitting
from customEffects import boostModListByReq
type = ("gang", "active")

def gangGasHarvesterAndIceHarvesterAndMiningLaserDurationBonus(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "duration",
            "commandBonus",
            lambda mod: mod.group.name in ("Mining Laser", "Strip Miner", "Frequency Mining Laser", "Ice Harvester", "Gas Cloud Harvester"),
            self.item,
            useStackingPenalty = True
        )
