#Used by: Item: Blue Pill Booster
#               Exile Booster
from customEffects import boost
type = "boosterSideEffect"
def boosterCapacitorCapacityPenalty(self, fitting):
    boost(fitting.ship, "capacitorCapacity", "boosterCapacitorCapacityPenalty",
          self.item)