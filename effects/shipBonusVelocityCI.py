#Variations of item: Badger (2 of 2) [Ship]
#Variations of item: Badger Mark II (2 of 2) [Ship]
from customEffects import boost
def shipBonusVelocityCI(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Industrial")
    boost(fitting.ship, "maxVelocity", "shipBonusCI", self.item,
          extraMult = level)