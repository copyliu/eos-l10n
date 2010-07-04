#Used by: Ship: Ark
from customEffects import boost
def freighterAgilityBonusA1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Freighter")
    boost(fitting.ship, "agility", "freighterBonusA1", self.item, extraMult = level)