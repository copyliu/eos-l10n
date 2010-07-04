#Used by: Item: All Missile Bays
from model.attribute import basicAttribute
from customEffects import increase
def launcherFitted(self, fitting, state):
    self.item.attributes['_hardpoint'] = basicAttribute(self.item, "_hardpoint", None, "launcher")
    self.item.attributes['_ammoConsumed'] = basicAttribute(self.item, "_ammoConsumed", None, True)
    increase(fitting.ship, 'launcherSlotsLeft', -1)
