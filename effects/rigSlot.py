#Items from market group: Ship Modifications > Rigs (462 of 462)
from model import attribute
def rigSlot(self, fitting, state):
    self.item.attributes['_slot'] = attribute.basicAttribute(self.item, "_slot", None, "rig")