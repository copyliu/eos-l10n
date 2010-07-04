#Used by: Ship: Bestower
#               Prorator
#               Impel
#               Sigil
from customEffects import boost
def shipCargoBonusAI(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Industrial")
    boost(fitting.ship, "capacity", "shipBonusAI", self.item, extraMult = level)