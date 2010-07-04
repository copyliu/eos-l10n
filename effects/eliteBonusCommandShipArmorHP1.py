#Used by: Ship: Damnation
from customEffects import boost
def eliteBonusCommandShipArmorHP1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boost(fitting.ship, "armorHP", "eliteBonusCommandShips1", self.item, extraMult = level)