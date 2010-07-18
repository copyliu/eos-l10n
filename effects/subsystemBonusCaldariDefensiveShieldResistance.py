#Item: Tengu Defensive - Adaptive Shielding [Subsystem]
from customEffects import boost
def subsystemBonusCaldariDefensiveShieldResistance(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Defensive Systems")
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        boost(fitting.ship, "shield" + resonanceType + "DamageResonance",
              "subsystemBonusCaldariDefensive", self.item, extraMult = level)