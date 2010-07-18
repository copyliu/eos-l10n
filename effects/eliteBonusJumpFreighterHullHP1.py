#Items from group: Jump Freighter (4 of 4) [Ship]
from customEffects import boost
def eliteBonusJumpFreighterHullHP1(self, fitting):
    skill, level = fitting.getCharSkill("Jump Freighters")
    boost(fitting.ship, "hp", "eliteBonusJumpFreighter1", self.item, extraMult = level)