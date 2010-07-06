#Used by: All modules that fit in a high slot
from model import attribute
def hiPower(self, fitting, state):
    self.item.attributes['_slot'] = attribute.basicAttribute(self.item, "_slot", None, "high")