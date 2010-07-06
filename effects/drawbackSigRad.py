#Used by: All shield related rigs
from customEffects import boost
def drawbackSigRad(self, fitting, state):
    boost(fitting.ship, "signatureRadius", "drawback", self.item)