#Items from group: Engineering Systems (16 of 16) [Subsystem]
#Items from group: Offensive Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import increase
def hardPointModifierEffect(self, fitting, state):
    increase(fitting.ship, "turretSlotsLeft", "turretHardPointModifier",
             self.item, position = "pre")
    increase(fitting.ship, "launcherSlotsLeft", "launcherHardPointModifier",
             self.item, position = "pre")