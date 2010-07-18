#Item: Advanced Spaceship Command
from customEffects import boost
def skillAdvancedSpaceshipAgilityBonus(self, fitting, level):
    if self.item in fitting.ship.requiredSkills:
        boost(fitting.ship, "agility", "agilityBonus", self.item, extraMult = level)