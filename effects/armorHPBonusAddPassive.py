#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import increase
def armorHPBonusAddPassive(self, fitting, state):
    increase(fitting.ship, "armorHP", "armorHPBonusAdd", self.item, position = "pre")
