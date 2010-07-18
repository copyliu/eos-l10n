#Items from category: Ship (25 of 245)
#Items from group: Carrier (4 of 4)
#Items from group: Dreadnought (4 of 4)
#Items from group: Freighter (4 of 4)
#Items from group: Jump Freighter (4 of 4)
#Items from group: Supercarrier (4 of 4)
#Items from group: Titan (4 of 4)
from customEffects import boost
def shipAdvancedSpaceshipCommandAgilityBonus(self, fitting):
    skill, level = fitting.getCharSkill("Advanced Spaceship Command")
    if skill:
        boost(fitting.ship, "agility", "agilityBonus", skill, extraMult = level)