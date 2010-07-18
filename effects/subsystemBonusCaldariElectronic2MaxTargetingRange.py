#Item: Tengu Electronics - Dissolution Sequencer [Subsystem]
from customEffects import boost
def subsystemBonusCaldariElectronic2MaxTargetingRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Electronic Systems")
    boost(fitting.ship, "maxTargetRange", "subsystemBonusCaldariElectronic2",
          self.item, extraMult = level)