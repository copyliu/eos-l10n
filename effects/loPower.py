#Used by: All modules that fit in a low slot
from model import attribute
def loPower(self, fitting, state):
    self.item.attributes['_slot'] = attribute.basicAttribute(self.item, "_slot", None, "low")
