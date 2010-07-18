#Item: Damnation
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipArmoredCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "commandBonus", "eliteBonusCommandShips2",
                           lambda skill: skill.name == "Armored Warfare Specialist",
                           self.item, extraMult = level)