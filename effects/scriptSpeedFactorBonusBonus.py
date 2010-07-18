#Item: Focused Warp Disruption [Charge]
from customEffects import boost
def scriptSpeedFactorBonusBonus(self, fitting, containerModule):
    boost(containerModule, "speedFactorBonus", "speedFactorBonusBonus", self.item)