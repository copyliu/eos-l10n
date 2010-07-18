#Items from category: Implant (11 of 471)
#Variations of item: Large Trimark Armor Pump I (2 of 2)
#Variations of item: Medium Trimark Armor Pump I (2 of 2)
#Variations of item: Small Trimark Armor Pump I (2 of 2)
#Item: Hull Upgrades
from customEffects import boost
def hullUpgradesArmorHpBonusPostPercentHpLocationShip(self, fitting, state = None, level = 1):
    boost(fitting.ship, "armorHP", "armorHpBonus", self.item, extraMult = level)