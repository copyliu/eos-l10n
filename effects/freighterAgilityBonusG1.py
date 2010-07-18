#Item: Anshar [Ship]
from customEffects import boost
def freighterAgilityBonusG1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Freighter")
    boost(fitting.ship, "agility", "freighterBonusG1", self.item, extraMult = level)