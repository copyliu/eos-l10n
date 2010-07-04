#Used by: Item: Black Hole Effect Beacon
type = "projected"
from customEffects import multiply
def systemAgility(self, fitting, state):
    multiply(fitting.ship, "agility", "agilityMultiplier", self.item)