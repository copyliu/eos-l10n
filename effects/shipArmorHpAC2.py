#Variations of item: Augoror (2 of 3) [Ship]
from customEffects import boost
def shipArmorHpAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boost(fitting.ship, "armorHP", "shipBonusAC2", self.item, extraMult = level)
