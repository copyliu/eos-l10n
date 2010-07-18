#Items from group: Engineering Systems (16 of 16)
runTime = "early"
from customEffects import increase
def rechargeRateAddPassive(self, fitting, state):
    increase(fitting.ship, "rechargeRate", "rechargeRate",
             self.item, position = "pre")