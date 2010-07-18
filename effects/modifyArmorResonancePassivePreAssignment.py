#Items from group: Defensive Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import multiply
def modifyArmorResonancePassivePreAssignment(self, fitting, state):
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        multiply(fitting.ship, "armor" + resonanceType + "DamageResonance",
              "passiveArmor" + resonanceType + "DamageResonance", self.item)