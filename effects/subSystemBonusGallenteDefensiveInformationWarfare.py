#Item: Proteus Defensive - Warfare Processor [Subsystem]
from customEffects import boostModListBySkillReq
def subSystemBonusGallenteDefensiveInformationWarfare(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Defensive Systems")
    boostModListBySkillReq(fitting.modules, "commandBonus", "subsystemBonusGallenteDefensive",
                           lambda skill: skill.name == "Information Warfare Specialist",
                           self.item, extraMult = level)