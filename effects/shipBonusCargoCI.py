#Variations of item: Badger (2 of 2)
#Variations of item: Badger Mark II (2 of 2)
from customEffects import boost
def shipBonusCargoCI(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Industrial")
    boost(fitting.ship, "capacity", "shipBonusCI", self.item,
          extraMult = level)