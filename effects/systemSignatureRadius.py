#Items from group: Effect Beacon (12 of 38)
type = "projected"
from customEffects import multiply
def systemSignatureRadius(self, fitting, state):
    multiply(fitting.ship, "signatureRadius", "signatureRadiusMultiplier", self.item)