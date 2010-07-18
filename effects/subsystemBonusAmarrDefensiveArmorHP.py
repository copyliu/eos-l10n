#Item: Legion Defensive - Augmented Plating [Subsystem]
from customEffects import boost
def subsystemBonusAmarrDefensiveArmorHP(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Defensive Systems")
    boost(fitting.ship, "armorHP", "subsystemBonusAmarrDefensive",
          self.item, extraMult = level)