#Item: Tengu Engineering - Augmented Capacitor Reservoir
from customEffects import boost
def subsystemBonusCaldariEngineeringCapacitorCapacity(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Engineering Systems")
    boost(fitting.ship, "capacitorCapacity", "subsystemBonusCaldariEngineering",
          self.item, extraMult = level)