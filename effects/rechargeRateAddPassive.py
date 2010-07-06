#Used by: Item: All Engineering subsystems
runTime = "early"
from customEffects import increase
def rechargeRateAddPassive(self, fitting, state):
    increase(fitting.ship, "rechargeRate", "rechargeRate",
             self.item, position = "pre")