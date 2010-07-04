#Used by: Item: Loki Electronics - Tactical Targeting Network
from customEffects import boost
def subsystemBonusMinmatarElectronic2ScanResolution(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boost(fitting.ship, "scanResolution", "subsystemBonusMinmatarElectronic2",
          self.item, extraMult = level)