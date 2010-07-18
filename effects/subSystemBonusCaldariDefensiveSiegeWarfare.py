#Item: Tengu Defensive - Warfare Processor [Subsystem]
from customEffects import boostModListBySkillReq
def subSystemBonusCaldariDefensiveSiegeWarfare(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Defensive Systems")
    boostModListBySkillReq(fitting.modules, "commandBonus", "subsystemBonusCaldariDefensive",
                           lambda skill: skill.name == "Siege Warfare Specialist",
                           self.item, extraMult = level)