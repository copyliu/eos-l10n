#Used by: Ship: Badger
#               Bustard
#               Crane
from customEffects import boost
def shipBonusCargoCI(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Industrial")
    boost(fitting.ship, "capacity", "shipBonusCI", self.item,
          extraMult = level)