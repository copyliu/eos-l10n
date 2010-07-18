#Item: Legion Electronics - Dissolution Sequencer
from customEffects import boost
def subsystemBonusAmarrElectronic2MaxTargetingRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boost(fitting.ship, "maxTargetRange", "subsystemBonusAmarrElectronic2",
          self.item, extraMult = level)