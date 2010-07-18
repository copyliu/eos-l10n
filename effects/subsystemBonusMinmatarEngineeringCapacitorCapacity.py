#Item: Loki Engineering - Augmented Capacitor Reservoir [Subsystem]
from customEffects import boost
def subsystemBonusMinmatarEngineeringCapacitorCapacity(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Engineering Systems")
    boost(fitting.ship, "capacitorCapacity", "subsystemBonusMinmatarEngineering",
          self.item, extraMult = level)