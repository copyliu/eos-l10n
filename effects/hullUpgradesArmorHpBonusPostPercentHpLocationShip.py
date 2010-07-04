#Used by: Skill: Hull Upgrades
#         Item : Trimark Armor Pump
#                Slave Implant Set
from customEffects import boost
def hullUpgradesArmorHpBonusPostPercentHpLocationShip(self, fitting, state = None, level = 1):
    boost(fitting.ship, "armorHP", "armorHpBonus", self.item, extraMult = level)