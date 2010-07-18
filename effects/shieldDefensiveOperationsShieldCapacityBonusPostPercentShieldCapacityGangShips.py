#Item: Siege Warfare [Skill]
#Item: Siege Warfare Mindlink [Implant]
from customEffects import boost
type = "gang"
def shieldDefensiveOperationsShieldCapacityBonusPostPercentShieldCapacityGangShips(self, fitting, level = 1):
    if self.item.group.name == "Cyber Leadership":
        skill, level = fitting.getCharSkill("Siege Warfare")
        if skill != None: fitting.gangSkills[skill]["level"] = 0
        level = 1

    boost(fitting.ship, "shieldCapacity", "shieldCapacityBonus", self.item, extraMult = level)
