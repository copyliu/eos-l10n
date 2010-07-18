#Items from group: Rig Shield (54 of 54) [Module]
from customEffects import boost
def drawbackSigRad(self, fitting, state):
    boost(fitting.ship, "signatureRadius", "drawback", self.item)