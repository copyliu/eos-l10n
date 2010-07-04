#Used by: Ship: Rhea
#               Nomad
#               Anshar
#               Ark
from customEffects import boost
def eliteBonusJumpFreighterArmorHP1(self, fitting):
    skill, level = fitting.getCharSkill("Jump Freighters")
    boost(fitting.ship, "armorHP", "eliteBonusJumpFreighter1", self.item, extraMult = level)