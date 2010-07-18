#Items from group: Armor Repair Projector (37 of 37)
#Items from group: Capacitor Booster (54 of 54)
#Items from group: Energy Destabilizer (41 of 41)
#Items from group: Energy Transfer Array (37 of 37)
#Items from group: Energy Vampire (52 of 52)
#Items from group: Hull Repair Unit (21 of 21)
#Items from group: Shield Transporter (38 of 38)
import model.fitting
from customEffects import boost
type = "overload"
def overloadSelfDurationBonus(self, fitting, state):
    if state >= model.fitting.STATE_OVERLOADED:
        boost(self.item, "duration", "overloadSelfDurationBonus", self.item)