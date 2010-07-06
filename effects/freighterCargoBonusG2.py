#Used by: Ship: Obelisk
#               Anshar
from customEffects import boost
def freighterCargoBonusG2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Freighter")
    boost(fitting.ship, "capacity", "freighterBonusG2", self.item, extraMult = level)