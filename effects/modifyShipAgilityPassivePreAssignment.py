#Used by: Item: All propulsion subsystems
runTime = "early"
from customEffects import multiply
def modifyShipAgilityPassivePreAssignment(self, fitting, state):
    fitting.ship.attributes["agility"].modifiedValue = self.item.getModifiedAttribute("agility")