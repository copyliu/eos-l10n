#Used by: Ship: Rhea
#               Nomad
#               Anshar
#               Ark
from customEffects import boost
def eliteBonusJumpFreighterHullHP1(self, fitting):
    skill, level = fitting.getCharSkill("Jump Freighters")
    boost(fitting.ship, "hp", "eliteBonusJumpFreighter1", self.item, extraMult = level)