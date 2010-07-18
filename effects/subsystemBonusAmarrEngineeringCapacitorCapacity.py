#Item: Legion Engineering - Augmented Capacitor Reservoir
from customEffects import boost
def subsystemBonusAmarrEngineeringCapacitorCapacity(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Engineering Systems")
    boost(fitting.ship, "capacitorCapacity", "subsystemBonusAmarrEngineering",
          self.item, extraMult = level)