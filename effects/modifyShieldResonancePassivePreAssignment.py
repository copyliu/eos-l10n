#Items from group: Defensive Systems (16 of 16) [Subsystem]
runTime = "early"
from customEffects import multiply
def modifyShieldResonancePassivePreAssignment(self, fitting, state):
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        multiply(fitting.ship, "shield" + resonanceType + "DamageResonance",
              "passiveShield" + resonanceType + "DamageResonance", self.item)