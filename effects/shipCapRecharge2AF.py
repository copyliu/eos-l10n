#Used by: Ship: Anathema
from customEffects import boost
def shipCapRecharge2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "rechargeRate", "shipBonus2AF", self.item, extraMult = level)