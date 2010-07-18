#Item: Multitasking [Skill]
#Item: Targeting [Skill]
from customEffects import increase
def targetingMaxTargetBonusModAddMaxLockedTargetsLocationChar(self, fitting, level):
    increase(fitting.ship, "_maxLockedTargetsSkill", "maxTargetBonus", self.item, extraMult = level)