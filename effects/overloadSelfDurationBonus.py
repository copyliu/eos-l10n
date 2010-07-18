#Items from group: Armor Repair Projector (37 of 37) [Module]
#Items from group: Capacitor Booster (54 of 54) [Module]
#Items from group: Energy Destabilizer (41 of 41) [Module]
#Items from group: Energy Transfer Array (37 of 37) [Module]
#Items from group: Energy Vampire (52 of 52) [Module]
#Items from group: Hull Repair Unit (21 of 21) [Module]
#Items from group: Shield Transporter (38 of 38) [Module]
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfDurationBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "duration", "overloadSelfDurationBonus", self.item)