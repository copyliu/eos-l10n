#Used by: Ship: Fenrir
from customEffects import boost
def freighterMaxVelocityBonusM1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Freighter")
    boost(fitting.ship, "maxVelocity", "freighterBonusM1", self.item, extraMult = level)