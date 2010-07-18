#Items from group: Capacitor Flux Coil (12 of 12)
#Items from group: Capacitor Power Relay (25 of 25)
#Items from group: Power Diagnostic System (31 of 31)
#Items from group: Reactor Control Unit (28 of 28)
#Items from group: Shield Flux Coil (11 of 11)
#Items from group: Shield Power Relay (11 of 11)
#Items from group: Shield Recharger (6 of 6)
import model.fitting
from customEffects import multiply
def modifyShieldRechargeRate(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "shieldRechargeRate", "shieldRechargeRateMultiplier", self.item)