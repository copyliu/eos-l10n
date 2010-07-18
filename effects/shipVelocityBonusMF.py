#Item: Vigil [Ship]
from customEffects import boost
def shipVelocityBonusMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boost(fitting.ship, "maxVelocity", "shipBonusMF", self.item, extraMult = level)