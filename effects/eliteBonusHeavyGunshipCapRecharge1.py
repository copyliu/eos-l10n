#Item: Sacrilege
from customEffects import boost
def eliteBonusHeavyGunshipCapRecharge1(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Assault Ships")
    boost(fitting.ship, "rechargeRate", "eliteBonusHeavyGunship1",
          self.item, extraMult = level)