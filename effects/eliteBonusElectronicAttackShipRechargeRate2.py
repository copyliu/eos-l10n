#Used by: Ship: Sentinel
from customEffects import boost
def eliteBonusElectronicAttackShipRechargeRate2(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boost(fitting.ship, "rechargeRate", "eliteBonusElectronicAttackShip2",
          self.item, extraMult = level)