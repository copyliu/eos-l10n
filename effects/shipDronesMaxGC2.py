#Item: Guardian-Vexor [Ship]
from customEffects import increase
def shipDronesMaxGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    increase(fitting.ship, "_maxActiveDrones", "shipBonusGC2",
             self.item, extraMult = level)
