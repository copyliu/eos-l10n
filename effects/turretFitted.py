#Items from category: Module (542 of 3488)
#Items from group: Energy Weapon (181 of 181) [Module]
#Items from group: Hybrid Weapon (197 of 197) [Module]
#Items from group: Mining Laser (17 of 17) [Module]
#Items from group: Projectile Weapon (141 of 141) [Module]
#Items from market group: Ship Equipment > Turrets & Bays (311 of 444)
from model.attribute import basicAttribute
from customEffects import increase
type = "active"
def turretFitted(self, fitting, state):
    self.item.attributes['_hardpoint'] = basicAttribute(self.item, "_hardpoint", None, "turret")
    if self.item.group.name == "Energy Weapon": ammoConsumed = False
    else: ammoConsumed = True
    self.item.attributes['_ammoConsumed'] = basicAttribute(self.item, "_ammoConsumed", None, ammoConsumed)
    increase(fitting.ship, 'turretSlotsLeft', -1)