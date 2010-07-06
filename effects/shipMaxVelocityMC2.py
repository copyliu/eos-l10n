#Used by: Ship: Stabber
#               Vagabond
from customEffects import boost
def shipMaxVelocityMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "maxVelocity", "shipBonusMC2", self.item, extraMult = level)