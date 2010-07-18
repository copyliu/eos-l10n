#Items from category: Module (542 of 3488)
from model.attribute import basicAttribute
from customEffects import increase
type = "active"
def turretFitted(self, fitting, state):
    self.item.attributes['_hardpoint'] = basicAttribute(self.item, "_hardpoint", None, "turret")
    if self.item.group.name == "Energy Weapon": ammoConsumed = False
    else: ammoConsumed = True
    self.item.attributes['_ammoConsumed'] = basicAttribute(self.item, "_ammoConsumed", None, ammoConsumed)
    increase(fitting.ship, 'turretSlotsLeft', -1)