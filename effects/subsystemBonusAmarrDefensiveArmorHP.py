#Used by: Item: Legion Defensive - Augmented Plating
from customEffects import boost
def subsystemBonusAmarrDefensiveArmorHP(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Defensive Systems")
    boost(fitting.ship, "armorHP", "subsystemBonusAmarrDefensive",
          self.item, extraMult = level)