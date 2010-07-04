#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def signatureRadiusPreAssignment(self, fitting, state):
    fitting.ship.attributes["signatureRadius"].modifiedValue = \
        self.item.getModifiedAttribute("signatureRadius")