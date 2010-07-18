#Item: Kitsune
from customEffects import boost
def eliteBonusElectronicAttackShipCapacitorCapacity2(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boost(fitting.ship, "capacitorCapacity", "eliteBonusElectronicAttackShip2",
          self.item, extraMult = level)