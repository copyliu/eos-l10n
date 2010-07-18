#Item: Focused Warp Disruption
from customEffects import boost
def scriptSpeedFactorBonusBonus(self, fitting, containerModule):
    boost(containerModule, "speedFactorBonus", "speedFactorBonusBonus", self.item)