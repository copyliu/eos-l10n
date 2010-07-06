#Used by: All capitals
from customEffects import boost
def shipAdvancedSpaceshipCommandAgilityBonus(self, fitting):
    skill, level = fitting.getCharSkill("Advanced Spaceship Command")
    if skill:
        boost(fitting.ship, "agility", "agilityBonus", skill, extraMult = level)