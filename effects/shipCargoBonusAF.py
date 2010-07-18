#Item: Tormentor
from customEffects import boost
def shipCargoBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "capacity", "shipBonusAF", self.item, extraMult = level)