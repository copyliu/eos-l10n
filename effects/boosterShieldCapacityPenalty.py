#Used by: Item: Blue Pill Booster
#               Sooth Sayer Booster
#               X-Instict Booster
#               Drop Booster
from customEffects import boost
type = "boosterSideEffect"
def boosterShieldCapacityPenalty(self, fitting):
    boost(fitting.ship, "shieldCapacity", "boosterShieldCapacityPenalty", self.item)