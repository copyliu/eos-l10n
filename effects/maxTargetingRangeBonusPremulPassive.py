#Used by: Item: Ionic Field Projector
from customEffects import multiply
def maxTargetingRangeBonusPremulPassive(self, fitting, state):
    multiply(fitting.ship, "maxTargetRange", "maxTargetRangeMultiplier",
             self.item, useStackingPenalty = True)