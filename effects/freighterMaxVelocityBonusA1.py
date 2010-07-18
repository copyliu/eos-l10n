#Item: Providence [Ship]
from customEffects import boost
def freighterMaxVelocityBonusA1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Freighter")
    boost(fitting.ship, "maxVelocity", "freighterBonusA1", self.item, extraMult = level)