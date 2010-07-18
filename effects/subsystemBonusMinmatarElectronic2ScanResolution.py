#Item: Loki Electronics - Tactical Targeting Network [Subsystem]
from customEffects import boost
def subsystemBonusMinmatarElectronic2ScanResolution(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boost(fitting.ship, "scanResolution", "subsystemBonusMinmatarElectronic2",
          self.item, extraMult = level)