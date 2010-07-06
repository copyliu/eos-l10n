#Used by: Ship: Augoror
#               Augoror Navy Issue
from customEffects import boost
def shipArmorHpAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boost(fitting.ship, "armorHP", "shipBonusAC2", self.item, extraMult = level)
