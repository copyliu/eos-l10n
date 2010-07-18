#Item: Proteus Electronics - Dissolution Sequencer [Subsystem]
from customEffects import boost
def subsystemBonusGallenteElectronic2MaxTargetingRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Electronic Systems")
    boost(fitting.ship, "maxTargetRange", "subsystemBonusGallenteElectronic2",
          self.item, extraMult = level)