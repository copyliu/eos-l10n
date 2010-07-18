#Item: Focused Warp Disruption
from customEffects import boost
def scriptDurationBonus(self, fitting, containerModule):
    boost(containerModule, "duration", "durationBonus", self.item)
    boost(containerModule, "speedFactorBonus", "speedFactorBonusBonus", self.item)