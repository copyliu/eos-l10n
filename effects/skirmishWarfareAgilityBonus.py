#Item: Skirmish Warfare
#Item: Skirmish Warfare Mindlink
from customEffects import boost
type = "gang"
def skirmishWarfareAgilityBonus(self, fitting, level = 1):
    if self.item.group.name == "Cyber Leadership":
        skill, level = fitting.getCharSkill("Skirmish Warfare")
        if skill != None: fitting.gangSkills[skill]["level"] = 0
        level = 1

    boost(fitting.ship, "agility", "agilityBonus", self.item, extraMult = level)
