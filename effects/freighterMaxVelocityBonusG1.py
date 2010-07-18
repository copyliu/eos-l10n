#Item: Obelisk [Ship]
from customEffects import boost
def freighterMaxVelocityBonusG1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Freighter")
    boost(fitting.ship, "maxVelocity", "freighterBonusG1", self.item, extraMult = level)