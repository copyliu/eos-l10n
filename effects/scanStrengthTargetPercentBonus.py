#Items from group: Projected ECCM (7 of 7)
import model.fitting
from customEffects import boost
type = ("projected", "active")
def scanStrengthTargetPercentBonus(self, fitting, state):
    if state >= model.fitting.STATE_ACTIVE and fitting.ship.getModifiedAttribute("disallowAssistance") != 1:
        boost(fitting.ship, "scanGravimetricStrength", "scanGravimetricStrengthPercent",
              self.item, useStackingPenalty = True)
        boost(fitting.ship, "scanLadarStrength", "scanLadarStrengthPercent",
              self.item, useStackingPenalty = True)
        boost(fitting.ship, "scanRadarStrength", "scanRadarStrengthPercent",
              self.item, useStackingPenalty = True)
        boost(fitting.ship, "scanMagnetometricStrength", "scanMagnetometricStrengthPercent",
              self.item, useStackingPenalty = True)