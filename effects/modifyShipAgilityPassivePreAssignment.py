#Items from group: Propulsion Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import multiply
def modifyShipAgilityPassivePreAssignment(self, fitting, state):
    fitting.ship.attributes["agility"].modifiedValue = self.item.getModifiedAttribute("agility")