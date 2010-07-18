#Item: Multitasking
#Item: Targeting
from customEffects import increase
def targetingMaxTargetBonusModAddMaxLockedTargetsLocationChar(self, fitting, level):
    increase(fitting.ship, "_maxLockedTargetsSkill", "maxTargetBonus", self.item, extraMult = level)