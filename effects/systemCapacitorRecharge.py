#Used by: Item: Pulsar Effect Beacon
#               Cataclysmic Effect Beacon
type = "projected"
from customEffects import multiply
def systemCapacitorRecharge(self, fitting, state):
    multiply(fitting.ship, "rechargeRate", "rechargeRateMultiplier", self.item)