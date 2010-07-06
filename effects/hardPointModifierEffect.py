#Used by: Item: Offensive & Engineering subsystems
runTime = "early"
from customEffects import increase
def hardPointModifierEffect(self, fitting, state):
    increase(fitting.ship, "turretSlotsLeft", "turretHardPointModifier",
             self.item, position = "pre")
    increase(fitting.ship, "launcherSlotsLeft", "launcherHardPointModifier",
             self.item, position = "pre")