#Used by: Item: All T3 subsystems
from customEffects import increase
def slotModifier(self, fitting, state):
    increase(fitting.ship, "lowSlots", "lowSlotModifier", self.item)
    increase(fitting.ship, "medSlots", "medSlotModifier", self.item)
    increase(fitting.ship, "hiSlots", "hiSlotModifier", self.item)