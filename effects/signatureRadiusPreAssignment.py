#Items from group: Defensive Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import increase
def signatureRadiusPreAssignment(self, fitting, state):
    fitting.ship.attributes["signatureRadius"].modifiedValue = \
        self.item.getModifiedAttribute("signatureRadius")