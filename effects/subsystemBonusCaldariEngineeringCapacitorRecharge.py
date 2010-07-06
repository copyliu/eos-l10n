#Used by: Item: Tengu Engineering - Capacitor Regeneration Matrix
from customEffects import boost
def subsystemBonusCaldariEngineeringCapacitorRecharge(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Engineering Systems")
    boost(fitting.ship, "rechargeRate", "subsystemBonusCaldariEngineering",
          self.item, extraMult = level)