#Item: Legion Defensive - Adaptive Augmenter [Subsystem]
from customEffects import boost
def subsystemBonusAmarrDefensiveArmorResistance(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Defensive Systems")
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        boost(fitting.ship, "armor" + resonanceType + "DamageResonance",
              "subsystemBonusAmarrDefensive", self.item, extraMult = level)