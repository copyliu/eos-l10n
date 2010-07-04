#Used by: Item: Grail Implant Set
#               Talon Implant Set
#               Spur Implant Set
#               Jackal Implant Set
from customEffects import boost
def scanStrengthBonusPercentPassive(self, fitting):
    radar = self.item.getModifiedAttribute("scanRadarStrengthPercent")
    if radar: boost(fitting.ship, "scanRadarStrength", radar)
    ladar = self.item.getModifiedAttribute("scanLadarStrengthPercent")
    if ladar: boost(fitting.ship, "scanLadarStrength", ladar)
    gravimetric = self.item.getModifiedAttribute("scanGravimetricStrengthPercent")
    if gravimetric: boost(fitting.ship, "scanGravimetricStrength", gravimetric)
    magnetometric = self.item.getModifiedAttribute("scanMagnetometricStrengthPercent")
    if magnetometric: boost(fitting.ship, "scanMagnetometricStrength", magnetometric)