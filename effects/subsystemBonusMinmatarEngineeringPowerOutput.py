#Item: Loki Engineering - Power Core Multiplier [Subsystem]
from customEffects import boost
def subsystemBonusMinmatarEngineeringPowerOutput(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Engineering Systems")
    boost(fitting.ship, "powerOutput", "subsystemBonusMinmatarEngineering",
          self.item, extraMult = level)