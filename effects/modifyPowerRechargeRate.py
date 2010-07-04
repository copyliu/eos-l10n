#Used by: Item: Cap Recharger
#               Capacitor Flux Coil
#               Capacitor Power Relay
import model.fitting
from customEffects import multiply
def modifyPowerRechargeRate(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        multiply(fitting.ship, "rechargeRate", "capacitorRechargeRateMultiplier", self.item)