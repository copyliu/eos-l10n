#Used by: Item: T3 subsystems
runTime = "early"
from customEffects import multiply
def modifyShieldResonancePassivePreAssignment(self, fitting, state):
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        multiply(fitting.ship, "shield" + resonanceType + "DamageResonance",
              "passiveShield" + resonanceType + "DamageResonance", self.item)