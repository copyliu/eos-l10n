#Variations of item: Large Ionic Field Projector I (2 of 2) [Module]
#Variations of item: Medium Ionic Field Projector I (2 of 2) [Module]
#Variations of item: Small Ionic Field Projector I (2 of 2) [Module]
from customEffects import multiply
def maxTargetingRangeBonusPremulPassive(self, fitting, state):
    multiply(fitting.ship, "maxTargetRange", "maxTargetRangeMultiplier",
             self.item, useStackingPenalty = True)