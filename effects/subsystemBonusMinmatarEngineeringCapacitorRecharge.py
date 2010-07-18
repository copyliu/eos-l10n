#Item: Loki Engineering - Capacitor Regeneration Matrix [Subsystem]
from customEffects import boost
def subsystemBonusMinmatarEngineeringCapacitorRecharge(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Engineering Systems")
    boost(fitting.ship, "rechargeRate", "subsystemBonusMinmatarEngineering",
          self.item, extraMult = level)