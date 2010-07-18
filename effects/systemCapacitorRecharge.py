#Items from group: Effect Beacon (12 of 38)
type = "projected"
from customEffects import multiply
def systemCapacitorRecharge(self, fitting, state):
    multiply(fitting.ship, "rechargeRate", "rechargeRateMultiplier", self.item)