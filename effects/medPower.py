#Used by: All modules using a medium powered slot
from model import attribute
def medPower(self, fitting, state):
    self.item.attributes['_slot'] = attribute.basicAttribute(self.item, "_slot", None, "medium")