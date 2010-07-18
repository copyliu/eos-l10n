#Item: Jump Drive Operation [Skill]
from customEffects import boost
def jumpDriveSkillsCapacitorNeedBonus(self, fitting, level):
    boost(fitting.ship, "jumpDriveCapacitorNeed", "jumpDriveCapacitorNeedBonus", self.item, extraMult = level)
