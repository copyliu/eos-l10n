#Items from group: Dreadnought (4 of 4) [Ship]
#Items from group: Freighter (4 of 4) [Ship]
#Items from group: Jump Freighter (4 of 4) [Ship]
#Items from group: Titan (4 of 4) [Ship]
#Items from market group: Ships > Carriers (8 of 8)
#Item: Rorqual [Ship]
from customEffects import boost
def shipAdvancedSpaceshipCommandAgilityBonus(self, fitting):
    skill, level = fitting.getCharSkill("Advanced Spaceship Command")
    if skill:
        boost(fitting.ship, "agility", "agilityBonus", skill, extraMult = level)