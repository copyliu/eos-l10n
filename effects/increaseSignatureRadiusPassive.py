#Used by: Item: Tech II Missiles
from customEffects import boost
def increaseSignatureRadiusPassive(self, fitting, containerModule):
    boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)
