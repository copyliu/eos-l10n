#Used by: Ammo: Focused Warp Disruption
from customEffects import boost
def scriptSignatureRadiusBonusBonus(self, fitting, containerModule):
    boost(containerModule, "signatureRadiusBonus", "signatureRadiusBonusBonus", self.item)