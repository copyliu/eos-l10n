#Item: Charon [Ship]
from customEffects import boost
def freighterMaxVelocityBonusC1(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Freighter")
    boost(fitting.ship, "maxVelocity", "freighterBonusC1", self.item, extraMult = level)