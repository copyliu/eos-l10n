#Item: Burst [Ship]
from customEffects import boost
def shipCargoBonusMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boost(fitting.ship, "capacity", "shipBonusMF2", self.item, extraMult = level)