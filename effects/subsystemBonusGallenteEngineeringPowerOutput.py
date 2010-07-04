#Used by: Item: Proteus Engineering - Power Core Multiplier
from customEffects import boost
def subsystemBonusGallenteEngineeringPowerOutput(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Engineering Systems")
    boost(fitting.ship, "powerOutput", "subsystemBonusGallenteEngineering",
          self.item, extraMult = level)