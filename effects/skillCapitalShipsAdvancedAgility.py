#Item: Capital Ships [Skill]
from customEffects import boost
def skillCapitalShipsAdvancedAgility(self, fitting, level):
    if self.item in fitting.ship.requiredSkills:
        boost(fitting.ship, "agility", "agilityBonus", self.item, extraMult = level)