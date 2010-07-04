#Used by: Item: Proteus Electronics - Dissolution Sequencer
from customEffects import boost
def subsystemBonusGallenteElectronicScanStrengthMagnetometric(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Electronic Systems")
    boost(fitting.ship, "scanMagnetometricStrength", "subsystemBonusGallenteElectronic",
          self.item, extraMult = level)