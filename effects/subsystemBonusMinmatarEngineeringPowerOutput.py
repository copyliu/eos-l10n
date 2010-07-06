#Used by: Item: Loki Engineering - Power Core Multiplier
from customEffects import boost
def subsystemBonusMinmatarEngineeringPowerOutput(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Engineering Systems")
    boost(fitting.ship, "powerOutput", "subsystemBonusMinmatarEngineering",
          self.item, extraMult = level)