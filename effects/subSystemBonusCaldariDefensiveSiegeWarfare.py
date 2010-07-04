#Used by: Item: Tengu Defensive - Warfare Processor
from customEffects import boostModListBySkillReq
def subSystemBonusCaldariDefensiveSiegeWarfare(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Defensive Systems")
    boostModListBySkillReq(fitting.modules, "commandBonus", "subsystemBonusCaldariDefensive",
                           lambda skill: skill.name == "Siege Warfare Specialist",
                           self.item, extraMult = level)