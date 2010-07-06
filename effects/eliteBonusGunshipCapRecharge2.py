#Used by: Ship: Vengeance
from customEffects import boost
def eliteBonusGunshipCapRecharge2(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boost(fitting.ship, "rechargeRate", "eliteBonusGunship2", self.item,
          extraMult = level)