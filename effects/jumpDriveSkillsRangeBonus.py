#Item: Jump Drive Calibration [Skill]
from customEffects import boost
def jumpDriveSkillsRangeBonus(self, fitting, level):
    boost(fitting.ship, "jumpDriveRange", "jumpDriveRangeBonus", self.item, extraMult = level)
