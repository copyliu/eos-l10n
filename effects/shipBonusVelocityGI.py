#Items from market group: Ships > Industrial Ships > Gallente (5 of 7)
from customEffects import boost
def shipBonusVelocityGI(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Industrial")
    # Viator doesn't have GI bonus
    if "shipBonusGI" in fitting.ship.attributes:
        bonus = "shipBonusGI"
    else:
        bonus = "shipBonusGI2"
    boost(fitting.ship, "maxVelocity", bonus, self.item,
          extraMult = level)
