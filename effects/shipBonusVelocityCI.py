#Used by: Ship: Badger
#               Bustard
#               Crane
from customEffects import boost
def shipBonusVelocityCI(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Industrial")
    boost(fitting.ship, "maxVelocity", "shipBonusCI", self.item,
          extraMult = level)