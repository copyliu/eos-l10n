#Used by: Ship: Ishtar
from customEffects import increase
def eliteBonusHeavyGunshipDroneCapacity2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    increase(fitting.ship, "droneCapacity", "eliteBonusHeavyGunship2",
             self.item, extraMult = level)