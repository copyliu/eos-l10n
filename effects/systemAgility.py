#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
from customEffects import multiply
def systemAgility(self, fitting, state):
    multiply(fitting.ship, "agility", "agilityMultiplier", self.item)