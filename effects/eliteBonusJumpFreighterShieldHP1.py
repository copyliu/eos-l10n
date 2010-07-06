#Used by: Ship: Rhea
#               Nomad
#               Anshar
#               Ark
from customEffects import boost
def eliteBonusJumpFreighterShieldHP1(self, fitting):
    skill, level = fitting.getCharSkill("Jump Freighters")
    boost(fitting.ship, "shieldCapacity", "eliteBonusJumpFreighter1", self.item, extraMult = level)