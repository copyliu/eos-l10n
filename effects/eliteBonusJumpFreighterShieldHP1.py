#Items from group: Jump Freighter (4 of 4)
from customEffects import boost
def eliteBonusJumpFreighterShieldHP1(self, fitting):
    skill, level = fitting.getCharSkill("Jump Freighters")
    boost(fitting.ship, "shieldCapacity", "eliteBonusJumpFreighter1", self.item, extraMult = level)