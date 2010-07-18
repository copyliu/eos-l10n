#Item: Legion Engineering - Capacitor Regeneration Matrix [Subsystem]
from customEffects import boost
def subsystemBonusAmarrEngineeringCapacitorRecharge(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Engineering Systems")
    boost(fitting.ship, "rechargeRate", "subsystemBonusAmarrEngineering",
          self.item, extraMult = level)