#Used by: Item: Proteus Engineering - Capacitor Regeneration Matrix
from customEffects import boost
def subsystemBonusGallenteEngineeringCapacitorRecharge(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Engineering Systems")
    boost(fitting.ship, "rechargeRate", "subsystemBonusGallenteEngineering",
          self.item, extraMult = level)