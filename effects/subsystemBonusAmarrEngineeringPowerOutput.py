#Item: Legion Engineering - Power Core Multiplier
from customEffects import boost
def subsystemBonusAmarrEngineeringPowerOutput(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Engineering Systems")
    boost(fitting.ship, "powerOutput", "subsystemBonusAmarrEngineering",
          self.item, extraMult = level)