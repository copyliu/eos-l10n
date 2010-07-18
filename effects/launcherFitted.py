#Items from group: Missile Launcher Assault (12 of 12) [Module]
#Items from group: Missile Launcher Cruise (20 of 20) [Module]
#Items from group: Missile Launcher Heavy (12 of 12) [Module]
#Items from group: Missile Launcher Heavy Assault (12 of 12) [Module]
#Items from group: Missile Launcher Rocket (14 of 14) [Module]
#Items from group: Missile Launcher Siege (21 of 21) [Module]
#Items from group: Missile Launcher Standard (13 of 13) [Module]
#Items from market group: Ship Equipment > Turrets & Bays > Missile Launchers (44 of 44)
from model.attribute import basicAttribute
from customEffects import increase
def launcherFitted(self, fitting, state):
    self.item.attributes['_hardpoint'] = basicAttribute(self.item, "_hardpoint", None, "launcher")
    self.item.attributes['_ammoConsumed'] = basicAttribute(self.item, "_ammoConsumed", None, True)
    increase(fitting.ship, 'launcherSlotsLeft', -1)
