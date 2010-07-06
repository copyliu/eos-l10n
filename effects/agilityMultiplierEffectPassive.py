#Used by: Item: Polycarbon Engine Housing
from customEffects import boost
def agilityMultiplierEffectPassive(self, fitting, state):
    boost(fitting.ship, "agility", "agilityMultiplier", self.item,
          useStackingPenalty = True)