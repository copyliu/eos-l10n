#Used by: Skill: Armored Warfare
type = "gang"
from customEffects import boost
def armorTankingGang(self, fitting, level):
    boost(fitting.ship, "armorHP", "armorHpBonus", self.item, extraMult = level)