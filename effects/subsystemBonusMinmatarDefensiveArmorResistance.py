#Item: Loki Defensive - Adaptive Augmenter [Subsystem]
from customEffects import boost
def subsystemBonusMinmatarDefensiveArmorResistance(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Defensive Systems")
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        boost(fitting.ship, "armor" + resonanceType + "DamageResonance",
              "subsystemBonusMinmatarDefensive", self.item, extraMult = level)