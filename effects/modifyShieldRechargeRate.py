#Used by: Item: Power Diagnostic System
import model.fitting
from customEffects import multiply
def modifyShieldRechargeRate(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "shieldRechargeRate", "shieldRechargeRateMultiplier", self.item)