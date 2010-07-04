#Used by: Ship: Claymore
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipSkirmishCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "commandBonus", "eliteBonusCommandShips2",
                           lambda skill: skill.name == "Skirmish Warfare Specialist",
                           self.item, extraMult = level)