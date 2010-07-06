#Used by: Item: Loki Electronics - Dissolution Sequencer
from customEffects import boost
def subsystemBonusMinmatarElectronicScanStrengthLADAR(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boost(fitting.ship, "scanLadarStrength", "subsystemBonusMinmatarElectronic",
          self.item, extraMult = level)