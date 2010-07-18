#Items from group: Inertia Stabilizer (12 of 12) [Module]
from customEffects import boost
import model.fitting
def increaseSignatureRadiusOnline(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boost(fitting.ship, "signatureRadius", "signatureRadiusBonus", self.item)