#Used by: Ship: Fenrir
#               Nomad
from customEffects import boost
def freighterCargoBonusM2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Freighter")
    boost(fitting.ship, "capacity", "freighterBonusM2", self.item, extraMult = level)