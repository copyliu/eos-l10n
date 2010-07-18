#Item: Focused Warp Disruption [Charge]
from customEffects import boost
def scriptSignatureRadiusBonusBonus(self, fitting, containerModule):
    boost(containerModule, "signatureRadiusBonus", "signatureRadiusBonusBonus", self.item)