#Item: Nomad [Ship]
from customEffects import boost
def freighterAgilityBonusM1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Freighter")
    boost(fitting.ship, "agility", "freighterBonusM1", self.item, extraMult = level)