#Used by: Ship: Iteron
#               Viator
#               Occator
from customEffects import boost
def shipBonusCargo2GI(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Industrial")
    # The Iterons don't have the GI2 bonus.
    if "shipBonusGI2" in fitting.ship.attributes:
        bonus = "shipBonusGI2"
    else:
        bonus = "shipBonusGI"
    boost(fitting.ship, "capacity", bonus, self.item,
          extraMult = level)
