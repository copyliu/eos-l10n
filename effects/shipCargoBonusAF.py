#Used by: Ship: Tormentor
#Fly, oh thee tormentor. (go torment some roids, k k ?)
from customEffects import boost
def shipCargoBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "capacity", "shipBonusAF", self.item, extraMult = level)