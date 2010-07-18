#Item: Apocalypse Imperial Issue [Ship]
#Item: Paladin [Ship]
from customEffects import boost
def shipBonusCapCapAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boost(fitting.ship, "capacitorCapacity", "shipBonusAB2", self.item,
          extraMult = level)
