#Items from group: Electronic Systems (16 of 16)
runTime = "early"
from customEffects import increase
def scanStrengthAddPassive(self, fitting, state):
    increase(fitting.ship, "scanGravimetricStrength", "scanGravimetricStrength",
             self.item, position = "pre")
    increase(fitting.ship, "scanRadarStrength", "scanRadarStrength",
             self.item, position = "pre")
    increase(fitting.ship, "scanMagnetometricStrength", "scanMagnetometricStrength",
             self.item, position = "pre")
    increase(fitting.ship, "scanLadarStrength", "scanLadarStrength",
             self.item, position = "pre")