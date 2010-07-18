#Item: Legion Electronics - Dissolution Sequencer [Subsystem]
from customEffects import boost
def subsystemBonusAmarrElectronicScanStrengthRADAR(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boost(fitting.ship, "scanRadarStrength", "subsystemBonusAmarrElectronic",
          self.item, extraMult = level)