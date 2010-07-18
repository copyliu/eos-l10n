#Item: Probe [Ship]
from customEffects import boost
def shipCargoBonusMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boost(fitting.ship, "capacity", "shipBonusMF", self.item, extraMult = level)