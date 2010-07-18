#Variations of item: Apocalypse (2 of 4) [Ship]
from customEffects import boost
def shipBonusCapCapAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boost(fitting.ship, "capacitorCapacity", "shipBonusAB2", self.item,
          extraMult = level)
