#Used by: Ship: Bestower
#               Prorator
#               Impel
#               Sigil
from customEffects import boost
def shipVelocityBonusAI(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Industrial")
    boost(fitting.ship, "maxVelocity", "shipBonusAI", self.item,
          extraMult = level)