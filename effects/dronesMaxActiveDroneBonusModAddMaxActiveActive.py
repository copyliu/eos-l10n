#Item: Drone Control Unit I [Module]
from customEffects import increase
import model.fitting
type = 'active'

def dronesMaxActiveDroneBonusModAddMaxActiveActive(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE:
        increase(fitting.ship, "_maxActiveDrones", "maxActiveDroneBonus", self.item)
