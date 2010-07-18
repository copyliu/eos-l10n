#Item: Loki Electronics - Dissolution Sequencer
from customEffects import boost
def subsystemBonusMinmatarElectronic2MaxTargetingRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boost(fitting.ship, "maxTargetRange", "subsystemBonusMinmatarElectronic2",
          self.item, extraMult = level)