#Used by: Skill: Jump Drive Operation
from customEffects import boost
def jumpDriveSkillsCapacitorNeedBonus(self, fitting, level):
    boost(fitting.ship, "jumpDriveCapacitorNeed", "jumpDriveCapacitorNeedBonus", self.item, extraMult = level)
