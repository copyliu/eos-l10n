#Item: Eos [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipInfoCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "commandBonus", "eliteBonusCommandShips2",
                           lambda skill: skill.name == "Information Warfare Specialist",
                           self.item, extraMult = level)