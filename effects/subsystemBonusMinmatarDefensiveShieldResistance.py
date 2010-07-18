#Item: Loki Defensive - Adaptive Shielding
from customEffects import boost
def subsystemBonusMinmatarDefensiveShieldResistance(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Defensive Systems")
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        boost(fitting.ship, "shield" + resonanceType + "DamageResonance",
              "subsystemBonusMinmatarDefensive", self.item, extraMult = level)