#Item: Proteus Defensive - Augmented Plating [Subsystem]
from customEffects import boost
def subsystemBonusGallenteDefensiveArmorHP(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Defensive Systems")
    boost(fitting.ship, "armorHP", "subsystemBonusGallenteDefensive",
          self.item, extraMult = level)