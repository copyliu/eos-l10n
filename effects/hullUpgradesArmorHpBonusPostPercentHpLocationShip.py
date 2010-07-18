#Items from group: Cyberimplant (11 of 138) [Implant]
#Variations of item: Large Trimark Armor Pump I (2 of 2) [Module]
#Variations of item: Medium Trimark Armor Pump I (2 of 2) [Module]
#Variations of item: Small Trimark Armor Pump I (2 of 2) [Module]
#Item: Hull Upgrades [Skill]
from customEffects import boost
def hullUpgradesArmorHpBonusPostPercentHpLocationShip(self, fitting, state = None, level = 1):
    boost(fitting.ship, "armorHP", "armorHpBonus", self.item, extraMult = level)