#Used by: All rigs
from model import attribute
def rigSlot(self, fitting, state):
    self.item.attributes['_slot'] = attribute.basicAttribute(self.item, "_slot", None, "rig")