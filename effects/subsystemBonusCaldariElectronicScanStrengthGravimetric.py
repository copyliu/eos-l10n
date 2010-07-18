#Item: Tengu Electronics - Dissolution Sequencer [Subsystem]
from customEffects import boost
def subsystemBonusCaldariElectronicScanStrengthGravimetric(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Electronic Systems")
    boost(fitting.ship, "scanGravimetricStrength", "subsystemBonusCaldariElectronic",
          self.item, extraMult = level)