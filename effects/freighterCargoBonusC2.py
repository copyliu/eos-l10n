#Variations of item: Charon (2 of 2) [Ship]
from customEffects import boost
def freighterCargoBonusC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Freighter")
    boost(fitting.ship, "capacity", "freighterBonusC2", self.item, extraMult = level)