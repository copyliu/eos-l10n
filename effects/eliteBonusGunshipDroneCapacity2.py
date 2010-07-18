#Item: Ishkur
from customEffects import increase
def eliteBonusGunshipDroneCapacity2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    increase(fitting.ship, "droneCapacity", "eliteBonusGunship2", self.item,
          extraMult = level)