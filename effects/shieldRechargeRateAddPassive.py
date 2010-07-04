#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def shieldRechargeRateAddPassive(self, fitting, state):
    increase(fitting.ship, "shieldRechargeRate", "shieldRechargeRate",
             self.item, position = "pre")