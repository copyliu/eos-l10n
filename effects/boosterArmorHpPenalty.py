#Used by: Item: Crash Booster
#               X-Instinct Booster
#               Frentix Booster
#               Exile Booster
type = "boosterSideEffect"
from customEffects import boost
def boosterArmorHpPenalty(self, fitting):
    boost(fitting.ship, "armorHP", "boosterArmorHPPenalty", self.item)