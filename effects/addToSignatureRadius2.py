#Used by: Item: Shield Extender
import model.fitting
from customEffects import increase
def addToSignatureRadius2(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        increase(fitting.ship, "signatureRadius", "signatureRadiusAdd", self.item)