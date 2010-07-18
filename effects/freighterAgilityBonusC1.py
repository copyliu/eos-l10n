#Item: Rhea
from customEffects import boost
def freighterAgilityBonusC1(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Freighter")
    boost(fitting.ship, "agility", "freighterBonusC1", self.item, extraMult = level)