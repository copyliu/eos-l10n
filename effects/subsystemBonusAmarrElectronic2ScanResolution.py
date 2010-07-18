#Item: Legion Electronics - Tactical Targeting Network [Subsystem]
from customEffects import boost
def subsystemBonusAmarrElectronic2ScanResolution(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boost(fitting.ship, "scanResolution", "subsystemBonusAmarrElectronic2",
          self.item, extraMult = level)