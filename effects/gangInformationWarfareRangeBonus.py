#Item: Information Warfare Link - Recon Operation
from customEffects import boostModListByReq
import model.fitting
type = ("gang", "active")

def gangInformationWarfareRangeBonus(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        boostModListByReq(
            fitting.modules,
            "maxRange",
            "commandBonus",
            lambda mod: mod.group.name in ("Target Painter", "Tracking Disruptor", "Remote Sensor Damper", "ECM"),
            self.item,
            useStackingPenalty = True
        )
