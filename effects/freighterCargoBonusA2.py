#Used by: Ship: Providence
#               Ark
from customEffects import boost
def freighterCargoBonusA2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Freighter")
    boost(fitting.ship, "capacity", "freighterBonusA2", self.item, extraMult = level)