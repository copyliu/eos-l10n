#Item: Loki Defensive - Warfare Processor [Subsystem]
from customEffects import boostModListBySkillReq
def subSystemBonusMinmatarDefensiveSkirmishWarfare(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Defensive Systems")
    boostModListBySkillReq(fitting.modules, "commandBonus", "subsystemBonusMinmatarDefensive",
                           lambda skill: skill.name == "Skirmish Warfare Specialist",
                           self.item, extraMult = level)