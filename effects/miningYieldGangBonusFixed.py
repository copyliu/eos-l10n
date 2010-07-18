#Item: Mining Foreman [Skill]
#Item: Mining Foreman Mindlink [Implant]
from customEffects import boostModListBySkillReq
type = "gang"
def miningYieldGangBonusFixed(self, fitting, level = 1):
    if self.item.group.name == "Cyber Leadership":
        skill, level = fitting.getCharSkill("Mining Foreman")
        if skill != None: fitting.gangSkills[skill]["level"] = 0
        level = 1

    boostModListBySkillReq(fitting.modules, "miningAmount", "miningAmountBonus",
                            lambda skill: skill.name == "Mining",
                            self.item, extraMult = level)
