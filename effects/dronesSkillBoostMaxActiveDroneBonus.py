#Item: Drones
from customEffects import increase
def dronesSkillBoostMaxActiveDroneBonus(self, fitting, level):
    increase(fitting.ship, "_maxActiveDrones", "maxActiveDroneBonus",
             self.item, extraMult = level)