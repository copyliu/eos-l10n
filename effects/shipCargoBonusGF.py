#Item: Navitas [Ship]
from customEffects import boost
def shipCargoBonusGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boost(fitting.ship, "capacity", "shipBonusGF2", self.item, extraMult = level)