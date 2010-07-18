#Item: Tengu Engineering - Power Core Multiplier [Subsystem]
from customEffects import boost
def subsystemBonusCaldariEngineeringPowerOutput(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Engineering Systems")
    boost(fitting.ship, "powerOutput", "subsystemBonusCaldariEngineering",
          self.item, extraMult = level)