#Used by: Skill: Targeting
#                Multitasking
from customEffects import increase
def targetingMaxTargetBonusModAddMaxLockedTargetsLocationChar(self, fitting, level):
    increase(fitting.ship, "_maxLockedTargetsSkill", "maxTargetBonus", self.item, extraMult = level)