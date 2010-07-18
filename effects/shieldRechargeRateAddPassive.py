#Items from group: Defensive Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import increase
def shieldRechargeRateAddPassive(self, fitting, state):
    increase(fitting.ship, "shieldRechargeRate", "shieldRechargeRate",
             self.item, position = "pre")