#Used by: Item: Signal Distortion Amplifier
import model.fitting
from customEffects import boostModListByReq
def scanGravimetricStrengthBonus(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(
            fitting.modules,
            "scanGravimetricStrengthBonus",
            "scanStrengthBonus",
            lambda mod: mod.group.name == "ECM",
            self.item,
            useStackingPenalty = True
        )
