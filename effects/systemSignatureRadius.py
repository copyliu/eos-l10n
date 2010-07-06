#Used by: Item: Pulsar Effect Beacon
#               Wolf Rayet Effect Beacon
type = "projected"
from customEffects import multiply
def systemSignatureRadius(self, fitting, state):
    multiply(fitting.ship, "signatureRadius", "signatureRadiusMultiplier", self.item)