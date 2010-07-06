#Used by: All T3 subsystems
from model import attribute
def subSystem(self, fitting, state):
    self.item.attributes['_slot'] = attribute.basicAttribute(self.item, "_slot", None, "subsystem")