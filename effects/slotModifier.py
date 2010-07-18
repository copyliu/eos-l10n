#Items from category: Subsystem (80 of 80)
from customEffects import increase
def slotModifier(self, fitting, state):
    increase(fitting.ship, "lowSlots", "lowSlotModifier", self.item)
    increase(fitting.ship, "medSlots", "medSlotModifier", self.item)
    increase(fitting.ship, "hiSlots", "hiSlotModifier", self.item)