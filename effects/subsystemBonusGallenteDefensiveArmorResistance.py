#Used by: Item: Proteus Defensive - Adaptive Augmenter
from customEffects import boost
def subsystemBonusGallenteDefensiveArmorResistance(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Defensive Systems")
    for resonanceType in ("Em", "Kinetic", "Thermal", "Explosive"):
        boost(fitting.ship, "armor" + resonanceType + "DamageResonance",
              "subsystemBonusGallenteDefensive", self.item, extraMult = level)