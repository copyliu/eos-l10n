#Used by: Skill: Information Warfare
#          Item: Information Warfare Mindlink
from customEffects import boost
type = "gang"
def reconOperationsMaxTargetRangeBonusPostPercentMaxTargetRangeGangShips(self, fitting, level = 1):
    if self.item.group.name == "Cyber Leadership":
        skill, level = fitting.getCharSkill("Information Warfare")
        if skill != None: fitting.gangSkills[skill]["level"] = 0
        level = 1
        
    boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus", self.item, extraMult = level)
