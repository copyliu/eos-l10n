#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import multiply
def modifyArmorResonancePassivePreAssignment(self, fitting, state):
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        multiply(fitting.ship, "armor" + resonanceType + "DamageResonance",
              "passiveArmor" + resonanceType + "DamageResonance", self.item)