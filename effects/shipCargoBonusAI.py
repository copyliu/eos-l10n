#Variations of item: Bestower (2 of 2)
#Variations of item: Sigil (2 of 2)
from customEffects import boost
def shipCargoBonusAI(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Industrial")
    boost(fitting.ship, "capacity", "shipBonusAI", self.item, extraMult = level)