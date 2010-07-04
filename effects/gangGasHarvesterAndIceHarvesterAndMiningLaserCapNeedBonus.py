#Used by: Item: Mining Foreman Link - Harvester Capacitor Efficiency
import model.fitting
from customEffects import boostModListByReq
type = ("gang", "active")

def gangGasHarvesterAndIceHarvesterAndMiningLaserCapNeedBonus(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "capacitorNeed",
            "commandBonus",
            lambda mod: mod.group.name in ("Mining Laser", "Strip Miner", "Frequency Mining Laser", "Ice Harvester", "Gas Cloud Harvester"),
            self.item,
            useStackingPenalty = True
        )
