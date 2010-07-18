#Item: Mining Foreman Link - Mining Laser Field Enhancement [Module]
from customEffects import boostModListByReq
import model.fitting
type = ("gang", "active")

def gangMiningLaserAndIceHarvesterAndGasCloudHarvesterMaxRangeBonus(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "maxRange",
            "commandBonus",
            lambda mod: mod.group.name in ("Mining Laser", "Strip Miner", "Frequency Mining Laser", "Ice Harvester", "Gas Cloud Harvester"),
            self.item,
            useStackingPenalty = True
        )
