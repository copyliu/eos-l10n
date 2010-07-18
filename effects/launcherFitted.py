#Items from category: Module (106 of 3488)
#Items from group: Missile Launcher Cruise (20 of 20)
#Items from group: Missile Launcher Heavy Assault (12 of 12)
#Items from group: Missile Launcher Rocket (14 of 14)
#Items from group: Missile Launcher Siege (21 of 21)
#Items from group: Missile Launcher Standard (13 of 13)
from model.attribute import basicAttribute
from customEffects import increase
def launcherFitted(self, fitting, state):
    self.item.attributes['_hardpoint'] = basicAttribute(self.item, "_hardpoint", None, "launcher")
    self.item.attributes['_ammoConsumed'] = basicAttribute(self.item, "_ammoConsumed", None, True)
    increase(fitting.ship, 'launcherSlotsLeft', -1)
