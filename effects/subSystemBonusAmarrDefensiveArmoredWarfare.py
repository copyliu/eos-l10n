#Item: Legion Defensive - Warfare Processor
from customEffects import boostModListBySkillReq
def subSystemBonusAmarrDefensiveArmoredWarfare(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Defensive Systems")
    boostModListBySkillReq(fitting.modules, "commandBonus", "subsystemBonusAmarrDefensive",
                           lambda skill: skill.name == "Armored Warfare Specialist",
                           self.item, extraMult = level)